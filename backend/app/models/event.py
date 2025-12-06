from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ForeignKeyConstraint
from sqlalchemy.sql import func
from app.models.base import Base
from sqlalchemy.orm import relationship
from app.models.sub_type import SubType


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)  # Nom de l'événement obligatoire
    url = Column(String(500), nullable=True)  # Permet des URLs longues
    description = Column(String(1000), nullable=True)  # Augmenter la taille pour des descriptions complètes
    created_at = Column(DateTime, default=func.now())  # Timestamp automatique
    ville = Column(String(100), nullable=False) 
    adresse = Column(String(200), nullable=True) 
    code_postal = Column(String(5), nullable=True) 
    

    # Clé étrangère vers `Type`
    sub_type_id = Column(Integer, ForeignKey(SubType.id), nullable=False)
    ForeignKeyConstraint(['sub_type_id'], ['sub_type.id'], name='fk_sub_type_id')
    sub_type = relationship(SubType)  # Relation SQLAlchemy


    def __repr__(self):
        return f"<Event(id={self.id}, name='{self.name}', type_id={self.sub_type_id}, date_debut={self.date_debut})>"