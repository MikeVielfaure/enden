from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TokenData(BaseModel):
    sub: str  # ID utilisateur
    role: Optional[str] = "user"  # Rôle par défaut "user"
    exp: Optional[datetime] = None  # Expiration du token