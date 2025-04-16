from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings

class Base(DeclarativeBase): pass

# 创建异步数据库引擎连接
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True
)

# 创建异步会话工厂
SessionLocal = sessionmaker(bind=engine)
