from pydantic import BaseModel, ConfigDict


class UserRequest(BaseModel):
    id: int
    username: str
    name: str
    role: str
    email: str | None = None
    phone: str | None = None
    status: int
    avatar: str | None = None
    model_config = ConfigDict(from_attributes=True)


# 用户信息响应模型（与 UserRequest 字段一致，独立命名便于后续扩展）
class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    role: str
    email: str | None = None
    phone: str | None = None
    status: int
    avatar: str | None = None
    model_config = ConfigDict(from_attributes=True)


class UserUpdateRequest(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    avatar: str | None = None
    model_config = ConfigDict(from_attributes=True)

class UserUpdatePasswordRequest(BaseModel):
    old_password: str
    password: str
    confirm_password: str
    model_config = ConfigDict(from_attributes=True)
