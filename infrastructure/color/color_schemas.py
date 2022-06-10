from pydantic import BaseModel


class ColorBase(BaseModel):
    user_number: int


class ColorCreate(BaseModel):
    red: int
    green: int
    blue: int
    user_number: int
    result: str


class Color(BaseModel):
    id: int
    red: int
    green: int
    blue: int
    user_number: int
    result: str

    class Config:
        orm_mode = True
