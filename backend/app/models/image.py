from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.models.event import Event

Base = declarative_base()

class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(500), nullable=False, unique=True)
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=func.now())

    # Clé étrangère vers Event avec une contrainte différée
    event_id = Column(Integer, ForeignKey(Event.id, ondelete="CASCADE"), nullable=False)
    event = relationship(Event)

    # Ajoutez la contrainte de clé étrangère avec 'use_alter=True' pour gérer les références croisées
    ForeignKeyConstraint(
        ['event_id'], 
        ['events.id'], 
        use_alter=True
    )

    def __repr__(self):
        return f"<Image(id={self.id}, url='{self.url}', event_id={self.event_id})>"
