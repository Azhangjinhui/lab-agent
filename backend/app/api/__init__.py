from fastapi import APIRouter
from app.api.user import router as user_router
from app.api.auth import router as auth_router
from app.api.flie import router as file_router
api = APIRouter(prefix='/api')

api.include_router(user_router)
api.include_router(auth_router)
api.include_router-(file_router)



