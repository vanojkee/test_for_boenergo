from sqlalchemy.orm import Session
from .color_models import Color
from .color_schemas import ColorCreate


def get_colors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Color).offset(skip).limit(limit).all()


def create_color(db: Session, color: ColorCreate):
    db_color = Color(**color.dict())
    db.add(db_color)
    db.commit()
    db.refresh(db_color)
    return db_color
