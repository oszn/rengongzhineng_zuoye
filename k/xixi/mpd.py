import matplotlib.pyplot as plt
from full.one_step import hip
import numpy as np
def draw():
    where,data=hip(4,100)
    c_dict={}
    for i in data:
        for j in i:
            if j not in c_dict:
                c_dict[j]=0
            c_dict[j]+=1
    d=[]
    for c in c_dict.keys():
       d.append([c,c_dict[c]])
    d=np.array(d)
    print(d)
    xxxx=np.argsort(-d[:,0])
    print(d[xxxx[0]])
    plt.scatter(x=d[:,0],y=d[:,1])
    plt.show()
draw()