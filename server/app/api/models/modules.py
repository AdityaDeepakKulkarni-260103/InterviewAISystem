from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app import db
Base = declarative_base()

class Modules(Base, db.Model):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    module_info = db.relationship("ModuleInfo", backref="module", lazy=True)

    def __init__(self,**kwargs):
        for property,value in kwargs.items():
            if hasattr(value,'__iter__') and not isinstance(value,str):
                value=value[0]
            setattr(self,property,value)

    def __repr__(self):
        return f"Module('{self.name}', '{self.description}')"
    