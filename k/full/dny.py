from sql.kmql import mysql
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import log_loss
mdb=mysql()
mdb.init()


def mxp(str):
    cur=mdb.db.cursor()
    cur.execute(str)
    p=list(cur.fetchall())
    return p;
# def read_sql():

def test_read_json():
    dikey={}
    with open("tmd.json",'r') as f:
        temp=json.loads(f.read())
        key=temp.keys()
        for k in temp.keys():
            d=mxp(temp[k])
            x=1
            tdpx={}
            for i in d:
                tdpx[i[0]]=x
                x+=1
            dikey[k]=tdpx
    return dikey
# test_read_json()
# //  "Speed_limit": "SELECT DISTINCT Speed_limit FROM acident;",
def read_files():
    da = pd.read_csv('../data/accidents_2012_to_2014.csv/accidents_2012_to_2014.csv', sep=',')
    # c=da.loc[da['Speed_limit']==70]
    # # print(type(c))
    # da.loc[da['Speed_limit']==70,('Speed_limit')]='1'
    # print(da.loc[da['Speed_limit']=='1']['Speed_limit'])
    dk=test_read_json()
    for key in dk.keys():
        for j in dk[key].keys():
            j1=key
            if(key=='Pedestrian_Crossing_Human_Control'):
                j1="Pedestrian_Crossing-Human_Control"
            if(key=='Pedestrian_Crossing_Physical_Facilities'):
                j1="Pedestrian_Crossing-Physical_Facilities"
            da.loc[da[j1]==j,(j1)]=int(dk[key][j])
    print(da.keys())
    da=da.fillna(0)
    nmd_ml=da[['Road_Type','Speed_limit','Police_Force','Accident_Severity','Number_of_Vehicles', 'Number_of_Casualties',
               'Junction_Control','Pedestrian_Crossing-Human_Control','Pedestrian_Crossing-Physical_Facilities', 'Light_Conditions',
               'Weather_Conditions', 'Road_Surface_Conditions',
               'Special_Conditions_at_Site', 'Carriageway_Hazards',
               'Urban_or_Rural_Area', 'Did_Police_Officer_Attend_Scene_of_Accident',
               ]]
    # for i in nmd_ml.iterrows():
    #     print(i)
    dyx = [4000, 4000, 4000]

    x_train, X_test, y_train, y_test = train_test_split(nmd_ml.drop(columns=['Accident_Severity']).values,
                                                        nmd_ml['Accident_Severity'].values, test_size=0.2,
                                                        random_state=99)
    print("1")
    X_train=[]
    Y_train=[]
    print(x_train[0])
    # X_train=x_train
    # Y_train=y_train
    return x_train,y_train,X_test,y_test
    for i in range(len(x_train)):
        if(dyx[y_train[i]-1]>0):
            X_train.append(x_train[i])
            Y_train.append(y_train[i])
            dyx[y_train[i]-1]-=1
X_train, Y_train,X_test,y_test=read_files()
def logical():
    lr=LogisticRegression()
    lr.fit(X_train,Y_train)
    y_pred=lr.predict(X_test)
    print(lr.score(X_test,y_test))
# logical()
def randforest():
    # X_train, Y_train,X_test,y_test=
    random_forest=RandomForestClassifier(n_estimators=200)
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
randforest()
# read_files()