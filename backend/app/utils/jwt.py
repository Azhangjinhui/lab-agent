
from datetime import timedelta, datetime

import jwt

from app.config import settings


def create_access_token(user_id: int) -> str:
    expire = datetime.now() + timedelta(hours=settings.JWT_EXPIRE_HOURS)
    payload = {"user_id": user_id, "exp": expire}  # exp是固定key，不能写成别的
    return jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )

def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
        user_id = payload.get('user_id')
        if not user_id:
            raise jwt.InvalidTokenError('Invalid token')
        return {'user_id': user_id}
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError('Invalid token')
