from calL.dis import haversine
from sql.kmql import mysql
import pandas as pd
import json
import threading
import time
import numpy as np
Mysql=mysql()
Mysql.init()
f=open("sl.json",'r')
kp=json.loads(f.read())
map_key={"3":"A"}
cur = Mysql.db.cursor()
cur.execute(kp['s_3p'])
orgin_data = cur.fetchall()

string = kp['s_r2p']
patch = 1
class mThread(threading.Thread):
    def init(self,id,start,end):
        self.id=id
        self.st=start
        self.end=end
    def run(self):
        self.thread_cal(self.st,self.end)
    def thread_cal(self,start, end):
        patch = 1
        # print(start,end)
        Mysql = mysql()
        Mysql.init()
        cur=Mysql.db.cursor()
        for rmp in range(start, end, 1):
            i = orgin_data[rmp]
            patch += 1
            # print("x")
            try:
                cur.execute(string % ('\'A' + i[3] + '\''))
                if patch % 100 == 0:
                    print(patch, self.id)
                dj = cur.fetchall()
                distances = []
                # print(1)
                for j in dj:
                    # print(j[2],j[1],i[1],i[0])
                    distances.append(haversine(float(j[2]), float(j[1]), float(i[1]), float(i[0])))
                wps = np.argsort(distances)
                sp = kp['wor']
                ex = sp % (dj[wps[0]][0], distances[wps[0]], i[2])

                # print(ex)
                cur.execute(ex)
                Mysql.db.commit()

            except Exception as e:
                print("?")
def cal_px():
    cur=Mysql.db.cursor()
    cur.execute(kp['s_3p'])
    orgin_data=cur.fetchall()

    string=kp['s_r2p']
    patch=1
    for rmp in range(7000,len(orgin_data),1):
        i=orgin_data[rmp]
        patch+=1
        try:
            cur.execute(string%('\'A'+i[3]+'\''))
            if patch%100==0:
                print(patch)
            dj=cur.fetchall()
            distances=[]
            for j in dj:
                # print(j[2],j[1],i[1],i[0])
                distances.append(haversine(float(j[2]),float(j[1]),float(i[1]),float(i[0])))
            wps=np.argsort(distances)
            sp=kp['wor']
            ex=sp%(dj[wps[0]][0],distances[wps[0]],i[2])
            print(ex)
            # print(ex)
            cur.execute(ex)
            Mysql.db.commit()
        except Exception as e:
            print("?")
    # print(string%(str(11)))
x=0
for i in range(7450,20000,400):
    m=mThread()
    m.init(x,i,i+400)
    m.start()
    print(x)

    x+=1
# cal_px()