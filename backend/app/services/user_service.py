from app.models.user import User
from app.schemas.user import UserResponse, UserUpdateRequest
from sqlalchemy.orm import Session



def get_user_info(user: User)->UserResponse:
    return UserResponse.model_validate(user)

def update_user_info(db: Session, user: User, data: UserUpdateRequest)->UserResponse:
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



