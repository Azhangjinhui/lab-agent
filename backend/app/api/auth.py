from fastapi import APIRouter,Depends

from app.schemas.auths import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserRequest
from app.common.response import Response
from app.common.exceptions import BusinessException
from app.utils.passwod import verify_password
from app.utils.jwt import create_access_token,decode_access_token
from app.schemas.auths import LoginResponse
from app.schemas.user import UserResponse


router = APIRouter(prefix='/auth',tags=['权限验证'])


@router.post('/login')
def login(data: LoginRequest,db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username==data.username).first()
    if not user or not verify_password(data.password,user.password):
        raise BusinessException('账号或密码错误')
    if user.status!=1:
        raise BusinessException('账号已被禁用')
    access_token = create_access_token(user.id)
    return Response.success(
        message="登录成功",
        data=LoginResponse(token=access_token, user=UserResponse.model_validate(user)),
    )
       
 