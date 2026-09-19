
from app.database import Base

from sqlalchemy import String,Integer
from sqlalchemy.orm import Mapped,mapped_column



class User(Base):
    __tablename__='users'
    __table_args__={'comment':'用户表'}
    username:Mapped[str]=mapped_column(String(50),index=True,unique=True,comment='用户名',nullable=False)
    password:Mapped[str]=mapped_column(String(255),comment='密码',nullable=False)
    name:Mapped[str]=mapped_column(String(50),comment='名称',nullable=False)
    role: Mapped[str]=mapped_column(String(50),comment='角色',nullable=False)
    email:Mapped[str | None]=mapped_column(String(50),comment='邮箱')
    phone:Mapped[str | None]=mapped_column(String(50),comment='手机号')
    avatar:Mapped[str | None]=mapped_column(String(50),comment='头像')
    status:Mapped[int]=mapped_column(Integer,default=1,comment='状态')
    