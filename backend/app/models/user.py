from sqlalchemy import Column, Integer, String,  DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    mdp = Column(String)
    role = Column(String, default='user')
    created_at = Column(DateTime, default=func.now())
    google_id = Column(String, unique=True, index=True, nullable=True)