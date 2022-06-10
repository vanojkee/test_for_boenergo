from typing import Optional
from pydantic import BaseModel


class NumberBase(BaseModel):
    a: int
    b: int
    c: int


class NumberCreate(BaseModel):
    a: int
    b: int
    c: int
    sqrt1: Optional[float]
    sqrt2: Optional[float]


class Number(BaseModel):
    id: int
    a: int
    b: int
    c: int
    sqrt1: Optional[float]
    sqrt2: Optional[float]

    class Config:
        orm_mode = True
