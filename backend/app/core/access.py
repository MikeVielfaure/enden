from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.core.config import settings
from passlib.context import CryptContext
from app.models.user import User
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.schemas.token_data import TokenData
from sqlalchemy.orm import Session
from app.models.blacklist_token import TokenBlacklist


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

time_minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def blacklist_token(db: Session, token: str):
    db_token = TokenBlacklist(token=token)
    db.add(db_token)
    db.commit()

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: TokenData):
    # Conversion en dictionnaire pour l'encodage JWT
    to_encode = data.dict()
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        # Validation du token avec Pydantic
        token_data = TokenData(**payload)
        # Vérification de l'utilisateur en base de données
        user = db.query(User).filter(User.id == token_data.sub).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user  # Retourne l'utilisateur authentifié
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.mdp):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou mot de passe incorrect")
    return user


def create_refresh_token(data: TokenData):
    # Ajout de la durée d'expiration pour le refresh token (par exemple, 7 jours)
    expire = datetime.now() + timedelta(days=7)  # 7 jours d'expiration
    TokenData.exp = expire
    to_encode = data.dict()
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        # Validation du token avec Pydantic
        token_data = TokenData(**payload)
        # Vérification que le refresh token correspond à un utilisateur valide
        user = db.query(User).filter(User.id == token_data.sub).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user  # Retourne l'utilisateur authentifié
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired refresh token")
