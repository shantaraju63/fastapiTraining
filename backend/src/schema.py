from fastapi import FastAPI,HTTPException
from enum import Enum
from pydantic import BaseModel,Field,EmailStr,validator
from datetime import datetime
from info_error_log  import info_log,error_logs
import logging


class Status(str,Enum):
    booked="booked"
    avilable="avilable"


class Seates(BaseModel):
    seat_no:str=None
    status:Status

class Movie(BaseModel):
    
    title:str
    genre:str=None
    current_date:datetime
    seat:list[Seates]
    duration:int


    
    @validator("title")
    def is_email_list_empty(cls, title):
        try:
            if not title:
                raise ValueError("title is empty.")
            return title
        except Exception:
            error_logs()
            raise HTTPException(status_code=401,detail="reqired")

class Resp(Movie):
    id:str
    dayes_after:int
    relesedate:datetime

class Payment(str,Enum):
    upi="upi"
    cash="cash"
    
class Book(BaseModel):
    set_no:str
    name:str
    email:EmailStr
    payment_method:Payment
    price:int=Field(ge=300,default="300")
class Bresp(Book):
    id:str
    p_status:str


class Bookpatch(BaseModel):
    set_no:str=None
    name:str=None
    email:EmailStr=None
    payment_method:Payment=None
    price:int=None
class Brespatch(Bookpatch):
    id:str=None
    p_status:str=None

class Bookdata(BaseModel):
    isbn:str
    title:str
    author:str
    publication:str
