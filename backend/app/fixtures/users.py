from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.access import hash_password
from app.core.config import settings
from app.models.user import User
import logging

logger = logging.getLogger(__name__)

DATABASE_URL = settings.DATABASE_URL 
logger.critical(f'{DATABASE_URL}')  # Affiche l'URL de la base de données pour les logs
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_user(name='test', email='test@test.com', mdp='test', role='user', google_id=None):
    session = SessionLocal()
    try:
        logger.critical(f'{engine}')
        mdp = hash_password(mdp)
        user = User(
            name=name,
            email=email,
            mdp=mdp,
            role=role,
            google_id=google_id
        )
        session.add(user)
        session.commit()
        logger.critical("user créé avec succes.")
    except Exception as e:
        logger.error(f"Erreur lors de la création du user : {e}")
        raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


create_user()