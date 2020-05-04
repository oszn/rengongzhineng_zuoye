from xixi.caculate import cal
from sql.kmql import mysql
from full.json_read import get_sql
import numpy as np
def mmp(r1,r2,c1,c2,r,t):
    result=[]
    r=r*2
    for j in range(0,t+1,1):
        p=[]
        for i in range(0,t+1,1):
            # print(r1+(r/t)*i,c1+(r/t)*j)
            p.append([r1+(i/t)*r,c1-(j/t)*r])
        result.append(p)
    return result
def create_range(radios,times,center):
    r = cal(radios)
    # print(center)
    # print(center[0]-r,center[1]-r,11111)
    result = mmp(center[0] - r, center[0] + r,center[1] +r, center[1] - r, r, times)
    return result

def select_sql(center,radios):
    r=cal(radios)
    c1=center[0]-r
    c2=center[0]+r
    r1=center[1]+r
    r2=center[1]-r
    p=mysql()
    p.init()
    cur=p.db.cursor()
    string=get_sql("../full/sl.json","s_npp")
    cur.execute(string%(str(c1),str(c2),str(r1),str(r2)))
    data=cur.fetchall()
    data=np.array(data)
    return data[:,0:2]
def clear_data(dt,times,radios,center):
    #lat 51.471405135763256
    #lon -0.09187213576325076
    dp = 2 * cal(radios)
    lat=float(dt[0])
    lon=float(dt[1])
    o_lat=center[0]-dp/2
    o_lon=center[1]+dp/2
    la=lat-o_lat
    lo=o_lon-lon

    # print(dp)
    i=int(la/(dp/times))
    j=int(lo/(dp/times))
    return i,j
def hip(radios,times,center):
    data=select_sql(center,radios)
    result=np.zeros((times,times))
    for i in data:
        x,y=clear_data(i,times,radios,center)
        result[y][x]+=1;
    # print(result)
    rpx=create_range(radios,times,center)
    fial=[]

    for i in range(0,times,1):
        p=[]
        for j in range(0,times,1):
           temp=(rpx[i][j]+rpx[i+1][j]+rpx[i+1][j+1]+rpx[i][j+1])
           p.append([temp[0],temp[1]])
           # print(temp[0],temp[1])
#            if(not (temp[0]>=51.489391567881626
# and temp[0]<=51.52536443211838 and temp[1]<=-0.10985856788162537 and temp[1]>=-0.1458314321183746
# )):
#                print("err")

        fial.append(p)
    print(len(fial),len(fial[0]))
    print(result.shape)
    return fial,result
# select_sql()
hip(4,100,[51.507378,-0.127845])