from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.user import User
from app.schemas.user_schemas import UserCreate
from app.core.access import hash_password

router = APIRouter()


@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Vérifier si l'utilisateur existe déjà
    db_user_exist = db.query(User).filter(
        User.email == user.email,
        User.google_id.is_(None)  # Filtre pour éviter la confusion avec les comptes Google
    ).first()

    if db_user_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Un utilisateur avec cet email existe déjà."
        )

    # Hachage du mot de passe et création du nouvel utilisateur
    hash_mdp = hash_password(user.mdp)
    db_user = User(name=user.name, email=user.email, mdp=hash_mdp)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users