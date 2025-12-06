from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.event_shemas import EventSchema
from app.core.db import get_db
from app.models.event import Event

router = APIRouter()

@router.post("/events/", response_model=EventSchema)
def create_event(event: EventSchema, db: Session = Depends(get_db)):
    new_event = Event(name=event.name,
                      url=event.url,
                      description = event.description, 
                      date_debut = event.date_debut,
                      date_fin = event.date_fin,
                      type_id = event.type_id,
                      ville = event.ville,
                      adresse = event.adresse,
                      code_postal = event.code_postal)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)  # Recharge les données après l’insertion

    return new_event

@router.get("/events/{event_id}")
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_user = db.query(Event).filter(Event.id == event_id ).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_user

@router.get("/events/")
def get_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    return events