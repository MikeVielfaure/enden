from fastapi import APIRouter, Depends, HTTPException,  Request
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.schemas.user_schemas import UserLogin
from app.schemas.token_data import TokenData
from datetime import timedelta, datetime
from app.core.access import create_access_token, authenticate_user, create_refresh_token, blacklist_token, time_minutes
from fastapi.responses import JSONResponse

router = APIRouter()


# @router.post("/login/")
# async def login(request: Request):
#     body = await request.json()  # Récupérer le corps JSON de la requête
#     print(body)  # Imprimer le corps de la requête dans la console
#     return JSONResponse(content=body)


@router.post("/login/")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    try:
        print(user_data)  # Affiche les données reçues
        user = authenticate_user(db, user_data.email, user_data.mdp)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token_expires = datetime.now() + timedelta(minutes=time_minutes)
    access_token = create_access_token(data= TokenData(sub= str(user.id),role= user.role, exp=access_token_expires))
    refresh_token = create_refresh_token(data=TokenData(sub= str(user.id),role= user.role,)) 
    return {"access_token": access_token, "refresh_token":refresh_token, "token_type": "bearer"}


@router.post("/logout")
def logout(refresh_token: str, db: Session = Depends(get_db)):
    # Ajoute le Refresh Token à la liste noire
    blacklist_token(db, refresh_token)
    return {"message": "User logged out successfully"}