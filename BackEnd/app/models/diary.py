"""
    path: xiaoyi/BackEnd/app/models/diary.py
    description: 日记diary的模型
"""

from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, JSON
from app.core.database import Base


class Diary(Base):
    __tablename__ = 'diary'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='日记主体id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='日记标题')
    content: Mapped[str] = mapped_column(Text, nullable=False, comment='日记主体')
    image_url: Mapped[Optional[List[str]]] = mapped_column(JSON, default=None, nullable=True, comment='日记插图')