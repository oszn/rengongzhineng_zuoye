import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime
accident= pd.read_csv('../data/accidents_2012_to_2014.csv/accidents_2012_to_2014.csv', sep=',')
def ori():
    level3 = accident[accident['Accident_Severity'] == 3]
    level2 = accident[accident['Accident_Severity'] == 2]
    level1 = accident[accident['Accident_Severity'] == 1]
    f, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,9))

    ## level 3 plot
    level3.plot(kind='scatter', x='Longitude',y ='Latitude',
                    color='yellow',
                    s=.02, alpha=.6, subplots=True, ax=ax1)
    ax1.set_title("level_3_severtiy")
    ax1.set_facecolor('black')
    ## level 2 plot
    level2.plot(kind='scatter', x='Longitude',y ='Latitude',
                    color='yellow',
                    s=.02, alpha=.6, subplots=True, ax=ax2)
    ax2.set_title("level_2_severtiy")
    ax2.set_facecolor('black')

    # level 1 plot

    level1.plot(kind='scatter', x='Longitude',y ='Latitude',
                    color='yellow',
                    s=.02, alpha=.6, subplots=True, ax=ax3)
    ax3.set_title("level_1_severtiy")
    ax3.set_facecolor('black')
    plt.show()
def create_times():
    begin=datetime.datetime(2017,11,11,0,0)
    end=datetime.datetime(2017,11,12,0,0)
    delat=end-begin
    result=[]
    for i in range(delat.seconds+480):
        f,b=str(begin.min+datetime.timedelta(seconds=i*180)).split(" ")
        h,m,s=b.split(":")
        result.append(h+":"+m)
    return result

def nmd(time1,time2,xx):
    print(time1)
    f1=accident[(accident['Time']>=time1)&(accident['Time']<=time2)]
    f,(ax1)=plt.subplots(1,1,figsize=(5,9))
    f1.plot(kind='scatter',x='Longitude',y ='Latitude',
                    color='yellow',
                    s=.02, alpha=.6, subplots=True, ax=ax1)
    ax1.set_title(time1)
    ax1.set_facecolor("black")
    plt.ylim((49,61))
    plt.xlim((-7,3))
    plt.savefig("img/"+str(xx)+".jpg")
# nmd()
def save_img():
    re=create_times()
    for i in range(368,len(re)-1,1):

        nmd(re[i],re[i+1],i)
# save_img()
ori()