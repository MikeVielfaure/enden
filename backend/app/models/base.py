# app/models/base.py
from sqlalchemy.ext.declarative import declarative_base

# Une seule Base pour tout le projet
Base = declarative_base()