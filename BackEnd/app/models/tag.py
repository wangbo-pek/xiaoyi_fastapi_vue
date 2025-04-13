"""
    path: xiaoyi/BackEnd/app/models/tag.py
    description: 文章标签
"""

from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Boolean
from app.core.database import Base
from app.models.association import note_tag, diary_tag

if TYPE_CHECKING:
    from app.models.diary_list import DiaryList
    from app.models.note_list import NoteList

class Tag(Base):
    __tablename__ = 'tag'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='标签id')
    name: Mapped[str] = mapped_column(String(64), nullable=False, unique=True, comment='标签名字')
    description: Mapped[Optional[str]] = mapped_column(String(64), nullable=False, default='默认描述文字', comment='标签描述')
    color: Mapped[str] = mapped_column(String(64), nullable=False, default='#2196f3', comment='标签颜色')
    created_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False, comment='创建时间')
    updated_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False, comment='修改时间')

    is_show: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, comment='标签是否可见')
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='是否被软删除')

    # Tag n:n NoteList
    notes_list:Mapped[List["NoteList"]] = relationship(
        secondary=note_tag,
        back_populates='tags'
    )

    # Tag n:n DiaryList
    diaries_list:Mapped[List["DiaryList"]] = relationship(
        secondary=diary_tag,
        back_populates='tags'
    )
