from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

DATABASE_URL = settings.DATABASE_URL 
logger.critical(f'{DATABASE_URL}')  # Affiche l'URL de la base de données pour les logs
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_tables():
    try:
        logger.critical(f'{engine}')
        Base.metadata.create_all(bind=engine)
        logger.critical("Tables créées avec succès.")
    except Exception as e:
        logger.error(f"Erreur lors de la création des tables : {e}")
        raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()