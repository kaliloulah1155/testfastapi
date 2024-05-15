from fastapi import APIRouter
from app.api.v1.routers import users as usr
router = APIRouter()

 # Inclure les routes définies dans users.py
router.include_router(usr.router, prefix="/users", tags=["Utilisateurs"])