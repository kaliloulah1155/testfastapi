import uvicorn
from fastapi import FastAPI
from app.api.v1.routers import index as ind
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()
# Obtenir les valeurs des variables d'environnement
app_title = os.getenv("APP_TITLE")
app_description = os.getenv("APP_DESCRIPTION")
app_version = os.getenv("APP_VERSION")

app = FastAPI(
    title=app_title,
    description=app_description,
    version=app_version
    )

app.include_router(ind.router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8002, reload=True)