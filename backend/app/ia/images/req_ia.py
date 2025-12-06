import requests
import base64

# Charger l'image
image_path = "affiche.jpg"
with open(image_path, "rb") as f:
    img_bytes = f.read()
img_base64 = base64.b64encode(img_bytes).decode("utf-8")

# Préparer la requête
prompt = "Analyse l'affiche et renvoie un JSON avec titre, date, heure, adresse, ville, description, url"
payload = {
    "image": img_base64,
    "text": prompt
}

# Envoyer au worker
response = requests.post("http://localhost:40000/predict", json=payload)

# Afficher la réponse
print(response.json())
