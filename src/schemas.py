from locale import currency
import string
from unicodedata import name
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    currency: str

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class SaleBase(BaseModel):
    state: str
    value: float
    fee: float
    currency: str
    client: str

class Sale(SaleBase):
    id: int
    class Config:
        orm_mode = True

# class SaleOut(SaleBase):
#     Sale: Sale

#     class Config:
#         orm_mode = True

class SaleCreate(SaleBase):
    pass

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id: Optional[str]
