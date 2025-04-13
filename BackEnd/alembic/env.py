import sys
from pathlib import Path

# 加入 app 模块路径
sys.path.append(str(Path(__file__).resolve().parents[1] / "app"))

from logging.config import fileConfig
from sqlalchemy import pool
from alembic import context

from app.core.config import settings
from app.core.database import Base
from app.models import *  # 确保 __init__.py 导入了所有模型

# 🔥 配置数据库 URL 来自 settings 而不是 alembic.ini
config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    """离线迁移模式"""
    url = settings.DATABASE_URL  # 这里改为你的动态读取
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """在线迁移模式"""
    from sqlalchemy import create_engine

    connectable = create_engine(
        settings.DATABASE_URL,
        poolclass=pool.NullPool,
        future=True,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
