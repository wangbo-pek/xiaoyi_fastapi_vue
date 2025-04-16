"""
    path: xiaoyi/BackEnd/app/models/diary_list.py
    description: 日记diary列表的模型
"""

from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Boolean, Integer
from BackEnd.app.core.database import Base
from BackEnd.app.models.association import diary_tag

if TYPE_CHECKING:
    from app.models.tag import Tag
    from app.models.diary import Diary

class DiaryList(Base):
    __tablename__ = 'diary_list'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='日记列表id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='日记标题')
    brief: Mapped[str] = mapped_column(String(100), nullable=False, comment='日记概要')
    cover_img: Mapped[str] = mapped_column(String(500), nullable=False, comment='日记封面图')
    created_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now,
                                                   nullable=False, comment='创建时间')
    updated_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now,
                                                   nullable=False, comment='修改时间')

    # 日记状态
    is_show: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, comment='日记是否可见')
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='是否被软删除')
    status: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='日记状态(草稿、发布)')

    # 统计字段
    view_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='浏览次数')
    reading_time: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='阅读时间')
    word_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='字数')

    # DiaryList n:n Tag
    tags:Mapped[List["Tag"]] = relationship(
        secondary=diary_tag,
        back_populates='diaries_list'
    )

    # DiaryList 1:1 Diary
    diary: Mapped["Diary"] = relationship(back_populates="diary_list", uselist=False)