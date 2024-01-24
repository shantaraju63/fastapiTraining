from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from schema import Bookdata
from short import create_id,create_json,reles_date
import json

path="C:/Users/SGovindappa/Desktop/backend/responses/mnc.json"
app=FastAPI()
@app.post("/create")
def csre(b:Bookdata):
    id=create_id()
    dtaa=jsonable_encoder(b)
    create_json(id,dtaa,path)
    return dtaa

@app.get("/read")
def read(id:str):
    try:
        with open(path,'r') as k:
            m=json.load(k)
            if id in m:
                return m[id]
            else:
                raise HTTPException(status_code=404,detail="id not found")
    except:
        raise HTTPException(status_code=404,detail="fil not found")
@app.put("/update")
def update(id:str,name:str):
    try:
        with open(path,'r') as k:
            m=json.load(k)
            if id in m:
                m[id]['title']=name
                with open(path,'w') as k:
                    json.dump(m,k,indent=4)
            else:
                raise JSONResponse(status_code=404,content="id not found")
    except:
        raise HTTPException(status_code=404,detail="fil not found")
    
@app.delete("/remove")
def remove(id:str):
    k=False
    try:
        with open(path,'r') as k:
            m=json.load(k)
            if id in m:
                k=True
                m.pop(id)
                with open(path,'w') as k:
                    json.dump(m,k,indent=4)
            if k==False:
                 raise HTTPException(status_code=404,detail="id not found")
                    
        

               
    except:
        raise HTTPException(status_code=404,detail="fil not found")
