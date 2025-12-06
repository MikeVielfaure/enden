from pydantic import BaseModel, HttpUrl
from typing import Optional

class ImageSchema(BaseModel):
    url: str
    description: Optional[str] = None

    class Config:
        from_attributes = True  # Permet de convertir depuis un modèle SQLAlchemy