from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from app import db

Base = declarative_base()

class ModuleInfo(Base, db.Model):
    __tablename__ = 'module_info'
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)

    def __init__(self,**kwargs):
        for property,value in kwargs.items():
            if hasattr(value,'__iter__') and not isinstance(value,str):
                value=value[0]
            setattr(self,property,value)

    def __repr__(self):
        return f"ModuleInfo('{self.module_id}', '{self.version}', '{self.release_date}')"