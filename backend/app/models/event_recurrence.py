from sqlalchemy import Column, Integer, Time, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base



class EventRecurrence(Base):
    __tablename__ = 'event_recurrence'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_date_id = Column(Integer, ForeignKey('event_date.id'), nullable=False)
    day_of_week = Column(Integer, nullable=False)  # 0=Dimanche ... 6=Samedi
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    created_at = Column(DateTime, default=func.now())

    # Relation
    event_date = relationship("EventDate", back_populates="recurrences")

    def __repr__(self):
        return f"<EventRecurrence(id={self.id}, event_date_id={self.event_date_id}, day_of_week={self.day_of_week})>"