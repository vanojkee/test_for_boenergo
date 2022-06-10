from sqlalchemy.orm import Session
from .sqrt_models import Number
from .sqrt_schemas import NumberCreate


def get_numbers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Number).offset(skip).limit(limit).all()


def create_number(db: Session, number: NumberCreate):
    db_number = Number(**number.dict())
    db.add(db_number)
    db.commit()
    db.refresh(db_number)
    return db_number
