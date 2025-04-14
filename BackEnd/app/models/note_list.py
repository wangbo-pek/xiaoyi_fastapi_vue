"""
    path: xiaoyi/BackEnd/app/models/note_list.py
    description: 文章笔记note列表的模型
"""

from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Boolean, Integer, ForeignKey
from app.core.database import Base
from app.models.association import note_tag

if TYPE_CHECKING:
    from app.models.note import Note
    from app.models.category import Category
    from app.models.tag import Tag


class NoteList(Base):
    __tablename__ = 'note_list'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='文章列表id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='文章标题')
    brief: Mapped[str] = mapped_column(String(100), nullable=False, comment='文章概要')
    cover_img: Mapped[str] = mapped_column(String(500), nullable=False, comment='文章封面图')
    created_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now,
                                                   nullable=False, comment='创建时间')
    updated_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now,
                                                   nullable=False, comment='修改时间')

    # 文章状态
    is_show: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, comment='文章是否可见')
    is_pinned: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='文章是否被置顶')
    is_recommended: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='文章是否被推荐')
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='是否被软删除')
    status: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='文章状态(草稿、发布)')

    # SEO
    slug: Mapped[str] = mapped_column(String(100), default=None, nullable=True, comment='URL名称')
    keyword: Mapped[str] = mapped_column(String(100), default=None, nullable=True, comment='关键字')
    description: Mapped[str] = mapped_column(String(300), default=None, nullable=True, comment='描述')

    # 统计字段
    view_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='浏览次数')
    like_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='点赞次数')
    dislike_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='被踩次数')
    reading_time: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='阅读时间')
    word_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='字数')

    # Note 1:1 NoteList
    note: Mapped["Note"] = relationship(back_populates='note_list', uselist=False)

    # Note n:1 Category
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'), nullable=False,
                                             comment='对应分类id')
    category: Mapped["Category"] = relationship(back_populates='notes_list')

    # NoteList n:n Tag
    tags: Mapped[List["Tag"]] = relationship(
        secondary=note_tag,
        back_populates='notes_list'
    )
