import pymysql
import pandas as pd

class mysql():
    def init(self):
        self.db=pymysql.connect("localhost","root","123456","pl")
    def insert(self):
        da = pd.read_csv('../data/ukTrafficAADF.csv/ukTrafficAADF.csv', sep=',')
        string="insert into mroad values"
        plist=[]
        p=1;
        cur=self.db.cursor()
        for row in da.iterrows():
            # print(''.join(row[1].values))
            if(p%1000==0):
                print(p)
            p+=1
            lp=[]
            for i in row[1].values:
                lp.append('\''+str(i).replace('\'','')+'\'')
            data=",".join(lp)
            # print(data)
            try:
                cur.execute(string+'('+data+')')
                self.db.commit()
            except:
                pass
            # plist.append('('+data+')')
            # print('('+data+')')
        # string+=','.join(plist)
        #
        # cur.execute(string)
        # self.db.commit()
    def create_table(self):
        da = pd.read_csv('../data/ukTrafficAADF.csv/ukTrafficAADF.csv', sep=',')
        string = "create table mroad( "
        s1 = " varchar(50),"
        x=1
        for i in da:
            i=i.replace('-','_')
            # if("(District)" in i):
            #     i=i.replace("(District)",'1')
            # if("(Highway)" in i):
            #     i=i.replace("(Highway)",'2')
            string+=(i+s1)
        print(string)
        tmp_str=list(string)
        tmp_str[-1]=')'
        string=''.join(tmp_str)
        cur=self.db.cursor()
        cur.execute(string)
        self.db.commit()
# p=mysql()
# p.init()
# p.insert()
# p.create_table()