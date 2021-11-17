from typing import Optional
from pydantic import BaseModel,EmailStr 


class UserCreate(BaseModel):
    username : str 
    email : EmailStr
    password : str 


class ShowUser(BaseModel): # serializer
    username : str 
    email : EmailStr
    is_active : bool 

    class Config(): # convert to dictionary type
        orm_mode = True