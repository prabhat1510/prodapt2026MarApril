from pydantic import BaseModel, EmailStr
from typing import Optional


class Login(BaseModel):
    username: str
    password: str

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    phone: str

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str

class UserDetails(BaseModel):
    username: str
    firstName:str
    lastName:str
    email: EmailStr
    password:str
    phone: str
    homeAddress: Address
    workAddress: Optional[Address] = None
    otherAddress: Optional[list[Address]] = []
    roles: list[str]
    #One user many restaurants
    restaurant_ids: Optional[list[str]] = []

class LoginResponse(BaseModel):
    #roles list of Role 
    roles: list[str]
    access_token: str
    refresh_token: str
    token_type: str

