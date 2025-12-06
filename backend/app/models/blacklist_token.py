from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.db import Base

class TokenBlacklist(Base):
    __tablename__ = 'token_blacklist'
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)
    revoked_at = Column(DateTime, default=datetime.now)  # Date et heure de l'invalidation