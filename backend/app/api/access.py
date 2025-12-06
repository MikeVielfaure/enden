from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.token_data import TokenData
from app.models.user import User
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.core.access import create_access_token, create_refresh_token, verify_refresh_token, blacklist_token, time_minutes
from datetime import timedelta, datetime
from app.models.blacklist_token import TokenBlacklist

router = APIRouter()


@router.post("/refresh_token/")
def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    # Vérifie le refresh token
    blacklisted_token = db.query(TokenBlacklist).filter(TokenBlacklist.token == refresh_token).first()
    if blacklisted_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has been revoked")
    user = verify_refresh_token(refresh_token, db)
    # Crée un nouveau refresh token
    new_refresh_token = create_refresh_token(TokenData(sub=user.id))
    blacklist_token(db, refresh_token)
    access_token_expires = datetime.now() + timedelta(minutes=time_minutes)
    # Crée un nouveau access token
    new_access_token = create_access_token(data= TokenData(sub= str(user.id),role= user.role, exp=access_token_expires))
    return {"access_token": new_access_token, "refresh_token": new_refresh_token}
