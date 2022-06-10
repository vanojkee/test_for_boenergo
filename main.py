from typing import List

import uvicorn
from fastapi import FastAPI, Depends, status

from sqlalchemy.orm import Session

from infrastructure.database import SessionLocal, engine
from infrastructure.database import Base

from infrastructure.sqrt.sqrt_schemas import Number, NumberBase, NumberCreate
from infrastructure.sqrt.sqrt_crud import get_numbers, create_number

from infrastructure.color.color_schemas import Color, ColorBase, ColorCreate
from infrastructure.color.color_crud import get_colors, create_color

from items import ColorItems, Sqrt

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/square", response_model=Number, status_code=status.HTTP_201_CREATED)
async def find_square(numbers: NumberBase, db: Session = Depends(get_db)):
    sq = Sqrt(a=numbers.a, b=numbers.b, c=numbers.c)
    sqrt1, sqrt2 = sq.find_square()

    return create_number(
        db=db,
        number=NumberCreate(
            a=numbers.a,
            b=numbers.b,
            c=numbers.c,
            sqrt1=sqrt1,
            sqrt2=sqrt2
        )
    )


@app.get("/squares/", response_model=List[Number], status_code=status.HTTP_200_OK)
async def read_squares(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    numbers = get_numbers(db, skip=skip, limit=limit)
    return numbers


@app.post("/color/", response_model=Color, status_code=status.HTTP_201_CREATED)
async def choice_color(colors: ColorBase, db: Session = Depends(get_db)):
    it = ColorItems()
    items = it.total_dict

    try:
        result = items[colors.user_number]

    except KeyError:
        result = 'no item'

    return create_color(
        db=db,
        color=ColorCreate(
            red=it.red,
            green=it.green,
            blue=it.blue,
            user_number=colors.user_number,
            result=result
        )
    )


@app.get("/colors/", response_model=List[Color], status_code=status.HTTP_200_OK)
async def read_colors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    colors = get_colors(db, skip=skip, limit=limit)
    return colors



if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
