from sqlalchemy import Column, Integer, Date, Time, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.models.event import Event
from app.models.event_recurrence import EventRecurrence

Base = declarative_base()

class EventDate(Base):
    __tablename__ = 'event_date'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)  # NULL si un seul jour
    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)
    created_at = Column(DateTime, default=func.now())

    # Relations
    event = relationship(Event, back_populates="dates")
    recurrences = relationship(
        EventRecurrence,
        back_populates="event_date",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<EventDate(id={self.id}, event_id={self.event_id}, start_date={self.start_date}, end_date={self.end_date})>"