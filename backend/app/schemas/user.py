from pydantic import BaseModel, ConfigDict



class UserRequest(BaseModel):
    id: int
    username: str
    name:str
    role:str
    email:str | None=None
    phone:str | None=None
    status:int
    model_config=ConfigDict(from_attributes=True)


# 用户信息响应模型（与 UserRequest 字段一致，独立命名便于后续扩展）
class UserResponse(BaseModel):
    id: int
    username: str
    name:str
    role:str
    email:str | None=None
    phone:str | None=None
    status:int
    model_config=ConfigDict(from_attributes=True)
    