from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.type_schemas import TypeSchema
from app.core.db import get_db
from app.models.type import Type

router = APIRouter()

@router.post("/types/", response_model=TypeSchema)
def create_type(type: TypeSchema, db: Session = Depends(get_db)):
    new_type = Type(libelle=type.libelle)
    db.add(new_type)
    db.commit()
    db.refresh(new_type)  # Recharge les données après l’insertion

    return new_type

@router.get("/types/{type_id}")
def read_type(type_id: int, db: Session = Depends(get_db)):
    db_user = db.query(Type).filter(Type.id == type_id ).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return db_user

@router.get("/types/")
def get_types(db: Session = Depends(get_db)):
    events = db.query(Type).all()
    return events