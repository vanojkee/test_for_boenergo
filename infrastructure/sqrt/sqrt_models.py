from sqlalchemy import Column, Integer, Float

from infrastructure.database import Base


class Number(Base):
    __tablename__ = "sqrt_logs"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Integer, index=True)
    b = Column(Integer, index=True)
    c = Column(Integer, index=True)
    sqrt1 = Column(Float, index=True)
    sqrt2 = Column(Float, index=True)
