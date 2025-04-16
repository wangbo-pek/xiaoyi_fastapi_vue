"""
    path: xiaoyi/BackEnd/app/models/category.py
    description: 文章分类模型
"""

from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Boolean
from BackEnd.app.core.database import Base

if TYPE_CHECKING:
    from app.models.note_list import NoteList

class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='分类id')
    name: Mapped[str] = mapped_column(String(64), nullable=False, unique=True, comment='分类名字')
    description: Mapped[Optional[str]] = mapped_column(String(64), nullable=False, default='默认描述文字', comment='分类描述')
    created_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False, comment='创建时间')
    updated_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False, comment='修改时间')

    is_show: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, comment='分类是否可见')
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='是否被软删除')

    # Category n:1 NoteList
    notes_list: Mapped[List["NoteList"]] = relationship(back_populates='category')