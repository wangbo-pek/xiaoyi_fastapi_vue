"""
    path: xiaoyi/BackEnd/app/models/note.py
    description: 文章笔记note的模型
"""

from typing import List, Optional, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, JSON, ForeignKey
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.note_list import NoteList

class Note(Base):
    __tablename__ = 'note'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='文章主体id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='文章标题')
    content:Mapped[str] = mapped_column(Text, nullable=False, comment='文章主体')
    image_url: Mapped[Optional[List[str]]] = mapped_column(JSON, default=None, nullable=True, comment='文章插图')

    # Note 1:1 NoteList
    note_list_id:Mapped[int] = mapped_column(ForeignKey('note_list.id'), nullable=False, unique=True, comment='对应note_list的id')
    note_list:Mapped["NoteList"] = relationship(back_populates='note', uselist=False)