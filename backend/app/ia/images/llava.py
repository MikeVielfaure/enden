from llava.model.builder import load_pretrained_model
from llava.mm_utils import process_images
from PIL import Image
import torch

model_path = "liuhaotian/llava-v1.5-7b"  # ou un autre checkpoint compatible
tokenizer, model, image_processor, _ = load_pretrained_model(
    model_path=model_path,
    model_base=None,
    model_name=model_path.split("/")[-1]
)

# Charger et pré‑traiter l'image
image = Image.open("affiche.jpg").convert("RGB")
pixel_values = image_processor(images=[image], return_tensors="pt").pixel_values

# Construire le prompt
prompt = "Analyse l'affiche et renvoie un JSON avec titre, date, heure, adresse, ville, description, url"

# Préparer les entrées
inputs = {
    "input": {
        "pixel_values": pixel_values
    },
    "prompt": prompt
}

with torch.no_grad():
    output = model.generate(**inputs)

print(output)