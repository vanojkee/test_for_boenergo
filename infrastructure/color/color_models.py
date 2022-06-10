from sqlalchemy import Column, Integer, String

from infrastructure.database import Base


class Color(Base):
    __tablename__ = "color_logs"

    id = Column(Integer, primary_key=True, index=True)
    red = Column(Integer, index=True)
    green = Column(Integer, index=True)
    blue = Column(Integer, index=True)
    user_number = Column(Integer, index=True)
    result = Column(String, index=True)
