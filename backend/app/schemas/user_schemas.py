from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Schéma pour la création d'un utilisateur (Inscription)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    mdp: str  # Mot de passe en clair (sera hashé côté backend)

# Schéma pour l'affichage d'un utilisateur (Réponse API)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    created_at: datetime
    google_id: Optional[str] = None

    class Config:
        from_attributes = True  # Permet la conversion SQLAlchemy -> Pydantic

# Schéma pour l'authentification (Connexion)
class UserLogin(BaseModel):
    email: str
    mdp: str  # Le mot de passe sera vérifié côté backend

# Schéma pour mettre à jour un utilisateur
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None

class UserCreateGmail(BaseModel):
    name: str
    email: EmailStr
    google_id: str