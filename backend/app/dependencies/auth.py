from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.utils.jwt import decode_access_token
def get_current_user(token:str = Depends(OAuth2PasswordBearer(tokenUrl='/api/auth/login')),db: Session = Depends(get_db)):
    # 解码access_token
    try:
        payload = decode_access_token(token)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='无效的access_token')
    user_id = payload.get('user_id')    
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='无效的access_token')
    # 查询用户
    user = db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='用户不存在')
    # 检查用户状态
    if user.status!=1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='账号已被禁用')
    return user
    
