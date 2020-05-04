from sql.kmql import mysql
import numpy as np
import matplotlib.pyplot as plt
def time_transform(time):
    h,m=time.split(":")
    h=int(h)
    m=int(m)
    return 60*h+m
def tran_time(n,div):
    time=n*div
    h=time/60
    m=time%60
    return str(h)+":"+str(m)
def get_time():
    p=mysql()
    p.init()
    cur=p.db.cursor()
    string="select Time from acident"

    cur.execute(string)
    time_data=cur.fetchall()
    time_dict={}
    npc=[]
    for i in list(time_data):
        npc.append(i[0])
    for i in npc:
        if i not in time_dict:
            time_dict[i]=0
        time_dict[i]+=1
    print(time_dict)
    times=np.zeros(24*60)
    n_time=np.zeros(24*6)
    for key in time_dict.keys():
        if(key!='nan'):
            times[time_transform(key)]=time_dict[key]
    for i in range(0, 24 * 60, 10):
        print(i)
        s=0
        for x in range(10):
            s+=times[i+x]
        n_time[int(i / 10)] =s
    x=[]
    for i in range(0,24*6):
        x.append(tran_time(i,10))
    x=range(0,24*6)

    plt.scatter(x,n_time)


    plt.show()

get_time()