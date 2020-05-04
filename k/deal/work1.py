import folium
import pandas as pd
from  folium import plugins
from sql.kmql import mysql
import json
import numpy as np
from xixi.caculate import cal
p = mysql()
p.init()
f=open('sql.json','r')
sqls=json.loads(f.read())
def gnmd(result):
    lix = []
    for i in result:
        lix.append(i)
    icd = folium.map.FeatureGroup()
    for i in lix:
        icd.add_child(
            folium.CircleMarker(
                i,
                radius=6,  # define how big you want the circle markers to be
                color='yellow',
                fill=True,
                fill_color='red',
                fill_opacity=0.4
            )
        )
    return  icd
def numper(result):
    icd=plugins.MarkerCluster()
    # result=[[ -0.152680,51.514570]]
    # lix=[]
    # for i in result:
    #     lix.append(i)
    # print(len(lix))
    print(result)
    for lat,lng,lable in result:
        folium.Marker(
            location=[lat,lng],
            icon=None,
            popup=str(lable)+','
        ).add_to(icd)
    return icd
from calL.dis import haversine
def mmp(r1,r2,c1,c2,r,t):
    result=[]
    r=r*2
    for i in range(0,t+1,1):
        for j in range(0,t+1,1):
            # print(r1+(r/t)*i,c1+(r/t)*j)
            result.append([r1+(i/t)*r,c1+(j/t)*r])
    return result
from full.one_step import hip
def get_limit(data,limit):
    c_dict = {}
    for i in data:
        for j in i:
            if j not in c_dict:
                c_dict[j] = 0
            c_dict[j] += 1
    d = []
    for c in c_dict.keys():
        d.append([c, c_dict[c]])
    d = np.array(d)
    # print(d)
    xxxx = np.argsort(-d[:, 0])
    a=0
    for i in xxxx:
       x=d[i]
       a=x[0]
       limit-=x[1]
       if(limit<0):
           break
    return a
def get_data(radios,times,center,control):
    where,data=hip(radios,times,center)
    p=[]
    limit=get_limit(data,10)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if(data[i][j]>=limit):
                if control==1:
                     where[i][j].append(data[i][j])
                p.append(where[i][j])
    x=[]
    for i in where:
        for j in i:
            x.append(j)
    return p,x
def total_common(p,c):
    x=[]
    for i in p:
       # x+=i
       result, a = get_data(4, 200, i,c)
       x+=result
    return x

def read_data():

    p.init()
    cur=p.db.cursor()
    cur.execute("SELECT Latitude,Longitude from acident where  1st_Road_Number in (select 1st_Road_Number from acident GROUP BY 1st_Road_Number HAVING count(1st_Road_Number)>2000) and 1st_Road_Class=3;")
    # result=cur.fetchall()
    r=cal(4)
    result = [[51.507378+r, -0.127845+r],[51.507378-r, -0.127845+r],[51.507378+r, -0.127845-r],[51.507378-r, -0.127845-r]]
    print(result)
    # result=mmp(51.507378-r,51.507378+r,-0.127845-r,-0.127845+r,r,20)##这个是算点的
    # 51.519500, -0.126849
    # print(result)
    #-0.075441,51.507887
    control=1
    result=total_common([[51.507887,-0.075441],[51.507378, -0.127845],[51.605549,-0.047845],[51.478997,-0.445686]],control)
    print(result)
    # print(haversine(result[2][0],result[2][1],result[1][0],result[1][1]))
    if control!=1:
        icd=gnmd(result)
    else:
        icd=numper(result)

    smp=folium.Map(location=[51.507378, -0.127845],zoom_start=12)
    # icd.add_to(smp)
    # icd.add_to(smp)
    # folium.GeoJson(
    #     "../data/js/x.geojson",
    #     style_function=lambda feature: {
    #         'fillColor': '#ffff00',
    #         'color': 'black',
    #         'weight': 2,
    #         'dashArray': '5, 5'
    #     }
    # ).add_to(smp)
    smp.add_child(icd)
    smp.save("t1/test3.html")
read_data()