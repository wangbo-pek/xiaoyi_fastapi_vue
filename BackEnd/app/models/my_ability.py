"""
    path: xiaoyi/BackEnd/app/models/my_ability.py
    description: 我的能力
"""

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class MyAbility(Base):
    __tablename__ = 'my_ability'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='我的能力id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的能力维度')
    description: Mapped[str] = mapped_column(String(100), nullable=False, comment='能力描述')
    degree: Mapped[int] = mapped_column(Integer, nullable=False, comment='掌握程度')
