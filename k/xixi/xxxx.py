f=open("1","r")
p=f.readlines()
x=[]
print(p)
for i in p:
    print(i)
    x.append(i.replace('\n',''))
print(",".join(x))