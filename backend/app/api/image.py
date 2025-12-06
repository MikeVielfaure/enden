import shutil
import os
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.schemas.image_shemas import ImageSchema
from app.core.db import get_db
from app.models.image import Image
from app.models.event import Event


router = APIRouter()

UPLOAD_DIR = "images/events/"  # Dossier de base pour les images
os.makedirs(UPLOAD_DIR, exist_ok=True)  

@router.post("/images/{event_id}/", response_model=ImageSchema)
def create_image(
    event_id: int, 
    file: UploadFile = File(...), 
    description: str = "", 
    db: Session = Depends(get_db)
):
    # Vérifier si l'événement existe
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Événement non trouvé")

    # Vérification du type de fichier
    allowed_extensions = {"png", "jpg", "jpeg", "gif"}
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Format d'image non supporté")

    # Création du dossier spécifique à l'événement
    event_folder = os.path.join(UPLOAD_DIR, str(event_id))
    os.makedirs(event_folder, exist_ok=True)  # Création si non existant

    # Définir le chemin de sauvegarde
    file_path = os.path.join(event_folder, file.filename)

    # Sauvegarde du fichier
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Sauvegarde en base de données
    new_image = Image(url=file_path, description=description, event_id=event_id)
    db.add(new_image)
    db.commit()
    db.refresh(new_image)

    return new_image

@router.get("/images/{image_id}")
def read_image(image_id: int, db: Session = Depends(get_db)):
    db_image = db.query(Image).filter(Image.id == image_id ).first()
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@router.get("/images/")
def get_images(db: Session = Depends(get_db)):
    events = db.query(Image).all()
    return events


@router.delete("/images/{image_id}", status_code=204)
def delete_image(image_id: int, db: Session = Depends(get_db)):
    # 🔹 Récupérer l’image depuis la base de données
    image = db.query(Image).filter(Image.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image non trouvée")

    # 🔹 Supprimer le fichier image
    image_path = image.url
    if os.path.exists(image_path):
        os.remove(image_path)

    # 🔹 Vérifier si le répertoire est vide et le supprimer
    event_folder = os.path.dirname(image_path)
    if os.path.exists(event_folder) and not os.listdir(event_folder):  # Vérifie si vide
        os.rmdir(event_folder)

    # 🔹 Supprimer l’image de la base de données
    db.delete(image)
    db.commit()

    return {"message": "Image supprimée avec succès"}