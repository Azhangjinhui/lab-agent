from app.common.exceptions import BusinessException
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdatePasswordRequest, UserUpdateRequest
from sqlalchemy.orm import Session

from app.utils.passwod import hash_password, verify_password


def get_user_info(user: User) -> UserResponse:
    return UserResponse.model_validate(user)


def update_user_info(db: Session, user: User, data: UserUpdateRequest) -> UserResponse:
    if data.name:
        user.name = data.name
    if data.email:
        user.email = data.email
    if data.phone:
        user.phone = data.phone
    if data.avatar:
        user.avatar = data.avatar
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)
def update_password(db: Session, user: User, data: UserUpdatePasswordRequest):
    """修改密码"""
    # 1. 验证旧密码
    if not verify_password(data.old_password, user.password):
        raise BusinessException("旧密码不正确", code=400)
    # 2. 校验两次新密码一致
    if data.password != data.confirm_password:
        raise BusinessException("两次输入的密码不一致", code=400)
    # 3. 哈希新密码并保存
    user.password = hash_password(data.password)
    db.commit()
    db.refresh(user)