from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings

class Base(DeclarativeBase): pass

# 创建数据库引擎连接
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    future=True,
    pool_pre_ping=True
)

# 创建数据库会话
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)