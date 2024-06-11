import datetime
from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, desc, Boolean, func, ForeignKey, TIMESTAMP

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)





