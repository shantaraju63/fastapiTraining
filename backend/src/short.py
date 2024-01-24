import json
import secrets
import string
from datetime import datetime
from datetime import datetime,date

def create_json(id,dict,path):
    try:

        with open(path,'r') as f1:
            data=json.load(f1)

    except FileNotFoundError as e:
        data={}
    data[id]=dict
    with open(path,'w') as k:
        json.dump(data,k,indent=4)

def create_id():
    char=string.ascii_letters+string.digits
    length=secrets.randbelow(4)+2
    rid="".join(secrets.choice(char)for i in range(length))
    return rid

def reles_date(path):
    n=str(datetime.today())
    with open(path,'r') as f3:
        k=json.load(f3)
        f=k['release_date']
        re=int(f[8:10])
        t=int(n[8:10])
        return t-re
