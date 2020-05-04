import json
def get_sql(file,sql):
    try:
        f=open(file,"r")
        kp=json.loads(f.read())
        return kp[sql]
    except Exception as e:
        print("error"+str(e))