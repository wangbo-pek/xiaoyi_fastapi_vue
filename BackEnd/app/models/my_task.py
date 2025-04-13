"""
    path: xiaoyi/BackEnd/app/models/my_task.py
    description: 我的任务
"""
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class MyTask(Base):
    __tablename__ = 'my_task'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='我的任务id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的任务名称')
    status: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='任务状态(未开始、进行中)')
    description: Mapped[str] = mapped_column(String(100), nullable=False, comment='任务描述')
    progress: Mapped[int] = mapped_column(Integer, nullable=False, comment='当前完成度')
    priority:Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='优先级')
    is_archived: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='是否完成')
    created_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now,
                                                   nullable=False, comment='创建时间')