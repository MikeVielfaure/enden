from pydantic import BaseModel
from datetime import datetime
from typing import  Optional
from app.schemas.image_shemas import ImageSchema

class EventSchema(BaseModel):
    name: str
    url: Optional[str] = None
    description: Optional[str] = None
    date_debut: datetime
    date_fin: Optional[datetime]
    type_id: int  # Clé étrangère vers `Type`
    ville: str
    adresse: Optional[str]
    code_postal: Optional[str]

    class Config:
        from_attributes = True  # Active la conversion SQLAlchemy -> Pydantic