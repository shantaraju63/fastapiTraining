from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel,ValidationError
from fastapi.encoders import jsonable_encoder
from schema import Movie,Resp,Book,Bresp,Brespatch
from short import create_id,create_json,reles_date
import json
from fastapi.security import OAuth2PasswordBearer
from info_error_log  import info_log,error_logs
import logging

app=FastAPI()

path="C:/Users/SGovindappa/Desktop/backend/responses/response.json"
res="C:/Users/SGovindappa/Desktop/backend/src/relese_date.json"
res="C:/Users/SGovindappa/Desktop/backend/src/relese_date.json"
bres="C:/Users/SGovindappa/Desktop/backend/responses/book.json"

with open(res,'r') as f:
    gk=json.load(f)
    l=gk['release_date']

@app.post("/create",response_model=Resp)
def create_movie(m:Movie):
    try:
        m.validate()
    except Exception:
        raise HTTPException(status_code=401,detail="reqired fields are mandatory")
    id=create_id()
    rel=reles_date(res)
    info=jsonable_encoder(m)
    info['id']=id
    info['dayes_after']=rel
    info['relesedate']=l
    create_json(id,info,path)
    info_log()
    '''hi'''
    return "hi"
    return info
    


@app.post("/booking",response_model=Bresp)
def book(b:Book):
    try:
        k=jsonable_encoder(b)
        id=create_id()
        k['id']=id
        p=k["price"]
        if(p>=300):
            k['p_status']='booked'
        else:
            k['p_status']="not bookrd"

        create_json(id,k,bres)
        return k
    except Exception:
        error_logs()
        raise HTTPException(status_code=401,detail="mn")
@app.get("/seatid")
def read_data(id:str):
    try:
        with open(bres,'r') as f2:
            data=json.load(f2)
            for i in data:
                if data[i]['set_no']==id:
                    return data[i]
                else:
                    raise HTTPException(status_code=404,detail="seat number not found")
    except Exception:
        raise HTTPException(status_code=404,detail="not found file")
# @app.get("/list")
# def list_items(title:str=None,seat:str=None,status:str=None):
#     m=[]
#     try:
#         with open(path,'r') as f3:
#             file=json.load(f3)
#     except Exception as e:
#         raise HTTPException(status_code=404,detail="file not found")
#     for _,info in file.items():
#         titles=info.get("title")
#         for i in range(len(info.get("seat"))):
#             json_seat = info.get("seat")[i]["seat_no"]

#         if((title==titles or title==None) and (seat==None or seat==json_seat) and(status==None or status==json_seat)):
#             extract={
#                 "title":info.get("title"),
#                 "genre":info.get("genre"),
#                 "current_date":info.get("current_date"),
#                 "seat":info.get("seat"),
#                 "duration":info.get("duration"),
#                 "id":info.get("id")
#             }
#             m.append(extract)
#     res=jsonable_encoder([Resp(**i) for i in m])
#     return res

@app.delete("/deleset")
def remove(set_nos:str):
    k=False
    try:
        with open(bres,'r') as d:
            var=json.load(d)
    except Exception as e:
        return HTTPException(status_code=404,detail="file not found")
    for k,i in var.items():
        if set_nos in i['set_no']:
            var.pop(k)
            with open(bres,"w") as f:
                json.dump(var,f,indent=4)

                with open(path,'r') as k1:
                    da=json.load(k1)
                    for j,l in da.items():
                        k=l.get('seat')
                        for s in range(len(k)):
                            if da[j]['seat'][s]['seat_no']==set_nos:
                                da[j]['seat'][s]['status']='avilable'
                                with open(path,'w') as cr:
                                    json.dump(da,cr,indent=4)
                return {'msg':'deleted key successfully'}
    else:
        return{"msg":"id not found"}
    


@app.patch("/update")
def update(id:str,p:Brespatch):
    conv=jsonable_encoder(p)
    conv['id']=id
    with open(bres,'r') as km:
        pt=json.load(km)
    nam=pt[id]['set_no']
    ag=pt[id]['name']
    ph=pt[id]['email']
    gen=pt[id]['payment_method']
    dj=pt[id]['price']
    p=pt[id]["p_status"]
    pt[id]=conv

        #for i in pt:
    if id in pt:
         if pt[id]['set_no']==None:
            pt[id]['set_no']=nam
         if(pt[id]["name"]==None):
            pt[id]["name"]=ag
         if pt[id]["email"]==None:
            pt[id]["email"]=ph
         if(pt[id]["payment_method"]==None):
            pt[id]["payment_method"]=gen
         if(pt[id]['price']==None):
            pt[id]['price']=dj
         if(pt[id]['p_status']==None):
            pt[id]['p_status']=p
    with open(bres,'w')as f3:
         json.dump(pt,f3,indent=4)
    return pt

fg=[]
Oauth2Schema=OAuth2PasswordBearer(tokenUrl="token")

@app.get("/list")
def get_list(name:str=None,seat_no:str=None,token:str=Depends(Oauth2Schema)):
    with open(path,'r') as d:
        data=json.load(d)
        for id,i in data.items():
            title=i.get("title")
            se=data[id]['seat'][0]["seat_no"]
            if(name==title or name==None ) and (se==seat_no or seat_no==None):
                extract_nam={
                    "title":i.get("title"),
                    "genre":i.get("genre"),
                    "current_date":i.get("current_date"),
                    "seat":i.get("seat"),
                    "duration":i.get("duration"),
                    "id":i.get("id"),
                    "dayes_after":i.get("dayes_after"),
                    "relesedate":i.get("relesedate")
                }
                fg.append(extract_nam)
    return fg