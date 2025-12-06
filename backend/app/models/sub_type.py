from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ForeignKeyConstraint
from app.models.type import Type


Base = declarative_base()


class SubType(Base):
    __tablename__ = 'sub_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(255), unique=True, nullable=False)
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=func.now())

    # Clé étrangère vers `Type`
    type_id = Column(Integer, ForeignKey(Type.id), nullable=False)
    ForeignKeyConstraint(['type_id'], ['types.id'], name='fk_type_id')
    type = relationship(Type)  # Relation SQLAlchemy



    