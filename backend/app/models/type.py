from sqlalchemy import Column, Integer, String, DateTime, func
from app.models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ForeignKeyConstraint


class Type(Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(255), unique=True, nullable=False)
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=func.now())


    def __repr__(self):
        return f"<Type(id={self.id}, libelle='{self.libelle}')>"
    




    