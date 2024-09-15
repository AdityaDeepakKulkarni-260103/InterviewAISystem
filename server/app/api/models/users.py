from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self,**kwargs):
        for property,value in kwargs.items():
            if hasattr(value,'__iter__') and not isinstance(value,str):
                value=value[0]
            setattr(self,property,value)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"