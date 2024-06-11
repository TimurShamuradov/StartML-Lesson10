from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
#from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:password@localhost/postgres")

Session = sessionmaker(autocommit=False, bind=engine, autoflush=False)

Base = declarative_base()

class User(Base):
    __tablename__ = "timur"
    first_name = Column(String, primary_key=True)
    last_name = Column(String)
    age = Column(Integer)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
