from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auths import LoginRequest, LoginResponse, RegisterRequest
from app.services import auth_service
from app.common.response import Response


router = APIRouter(prefix='/auth', tags=['权限验证'])







@router.post('/login')
def login(data: LoginRequest, db: Session = Depends(get_db)):
    result: LoginResponse = auth_service.login(db, data)
    return Response.success(
        message="登录成功",
        data=result,
    )
@router.post('/register')
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    auth_service.register(db, data)
    return Response.success(
        message="注册成功",
    )

