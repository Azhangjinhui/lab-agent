
from app.config import settings
from sqlalchemy import create_engine, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped
engine=create_engine(
    settings.DATABASE_URL,
    echo=True,
)
SessionLocal=sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)#数据库会话连接工厂
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    create_time:Mapped[datetime]=mapped_column(DateTime,default=datetime.now,comment='创建时间')
    update_time:Mapped[datetime]=mapped_column(DateTime,default=datetime.now,onupdate=datetime.now,comment='更新时间')
 