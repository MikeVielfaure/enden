# Étape 1 : Utilisation d'une image de base Python
FROM python:3.12-slim AS base

# Définir le répertoire de travail dans l'image Docker
WORKDIR /code

# Copier les fichiers pyproject.toml et poetry.lock
COPY pyproject.toml poetry.lock* /code/

# Installer Poetry
RUN pip install poetry

RUN poetry lock

# Installer les dépendances du projet sans les dépendances de développement
RUN poetry install --no-root


# Copier le code source de l'application dans le conteneur
COPY /app /code/app

#RUN poetry run python -m app.core.__init__
# Exposer le port de l'application
EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
