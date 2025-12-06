
from fastapi import FastAPI
from app.api.user import router as user
from app.api.event import router as event
from app.api.type import router as type
from app.api.image import router as image
from app.api.login import router as login
from app.core.config import settings

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



# Créer l'application FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise tout le monde (à restreindre en prod)
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les headers
)




@app.get("/")
def read_root():
    return {"message": f"{settings.DATABASE_URL}"}



# Ajouter les routers à l'application
app.include_router(user)
app.include_router(event)
app.include_router(type)
app.include_router(image)
app.include_router(login)