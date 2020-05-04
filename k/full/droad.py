import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import log_loss
from sql.kmql import mysql
import matplotlib.pyplot as plt
import sys
f=open("sl.json",'r')
kp=json.loads(f.read())
Mysql=mysql()
Mysql.init()
def read_data():
    cur=Mysql.db.cursor()
    string=kp['little_point']
    cur.execute(string)
    data=cur.fetchall()
    data=list(data)
    id_dict={}
    for i in range(len(data)):
        if data[i][0] not in id_dict:
            id_dict[data[i][0]]=[]
        id_dict[data[i][0]].append(i)

    string=kp['s_cn']
    car_dick={}
    car_data=[]
    for i in id_dict.keys():
        # print(string%(i))
        cur.execute(string%(i))
        car_=cur.fetchall()
        # print(car_)
        car_=list(car_)
        # print(car_)
        car_data.append(car_[0])
    for i in car_data:
        # print(i)
        temp=[]
        for x in range(2,len(i),1):
            temp.append(int(i[x]))
        temp=np.array(temp)
        temp=temp/temp.sum()
        # print(temp)
        if i[0] not in car_dick:
            car_dick[i[0]]=[]
        car_dick[i[0]].append(float(i[1]))
        for a in temp:
            car_dick[i[0]].append(float(a))
        # car_dick[i[0]]=temp
    return id_dict,car_dick
def inxp(p):
    # if p<10:
    #     return 2
    if p<5:
        return 1
    elif p<45:
        return 2
    else:
        return 3
def read_mp():

    id_, car_ = read_data()
    data=[]
    lable=[]
    for i in id_:
        lable.append(inxp((len(id_[i])/int(car_[int(i)][0]))*100000))
        # print(i)
        data.append(list(car_[int(i)]))

    # print(data)
    print(i)
    # print(lable)
    print(len(lable),len(data))
    # list(np.delete(data, 0, axis=1))
    x_train, X_test, y_train, y_test = train_test_split(data,lable, test_size=0.3,
                                                        random_state=99)
    # print(x_train,y_test,y_train,y_test)
    return x_train,y_train,X_test,y_test
def dpl():
    id_, car_ = read_data()
    data = []
    lable = []
    for i in id_:
        lable.append(int((len(id_[i]) / int(car_[int(i)][0])) * 100000))
        # print(i)
        data.append(list(car_[int(i)]))
    dictx={}
    for i in lable:
        if i not in dictx:
            dictx[i]=0
        dictx[i]+=1
    x=[]
    y=[]
    for k in dictx.keys():
        if k<200:
            x.append(k)
            y.append(dictx[k])
    return x,y
def draw():
    x,y=dpl()
    plt.scatter(x,y)
    plt.show()
def randforest():
    X_train, Y_train,X_test,y_test=read_mp()
    print(len(X_train))
    print(len(Y_train))
    print(Y_train)
    # print(Y_train)
    random_forest=RandomForestClassifier(n_estimators=200)
    print()
    random_forest.fit(X_train,Y_train)
    Y_pred=random_forest.predict(X_test)
    print(random_forest.feature_importances_)
    print(random_forest.score(X_test,y_test))
    acc_random_forest1 = round(random_forest.score(X_test, y_test) * 100, 2)

    sk_report = classification_report(
        digits=6,
        y_true=y_test,
        y_pred=Y_pred)
    print("Accuracy", acc_random_forest1)
    print(sk_report)
def anoe():
    id_,car_=read_data()
    for i in id_:
        print(len(id_[i]))
# read_data()
# read_mp()
# randforest()
# dpl()
draw()