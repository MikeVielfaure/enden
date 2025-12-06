from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ForeignKeyConstraint
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.models.type import Type

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)  # Nom de l'événement obligatoire
    url = Column(String(500), nullable=True)  # Permet des URLs longues
    description = Column(String(1000), nullable=True)  # Augmenter la taille pour des descriptions complètes
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=func.now())  # Timestamp automatique
    ville = Column(String(100), nullable=False) 
    adresse = Column(String(200), nullable=True) 
    code_postal = Column(String(5), nullable=True) 
    

    # Clé étrangère vers `Type`
    type_id = Column(Integer, ForeignKey(Type.id), nullable=False)
    ForeignKeyConstraint(['type_id'], ['types.id'], name='fk_type_id')
    type = relationship(Type)  # Relation SQLAlchemy


    def __repr__(self):
        return f"<Event(id={self.id}, name='{self.name}', type_id={self.type_id}, date_debut={self.date_debut})>"