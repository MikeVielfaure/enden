from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import List, Optional
from app.schemas.event_shemas import EventSchema

class TypeSchema(BaseModel):
    libelle : str
    description : Optional[str]
    created_at : datetime

    class Config:
        from_attributes = True  # Active la conversion SQLAlchemy -> Pydantic