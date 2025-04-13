"""
    path: xiaoyi/BackEnd/app/models/my_skill.py
    description: 我的技能
"""

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class MySkill(Base):
    __tablename__ = 'my_skill'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='我的技能id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的技能维度')
    description: Mapped[str] = mapped_column(String(100), nullable=False, comment='技能描述')
    degree: Mapped[int] = mapped_column(Integer, nullable=False, comment='掌握程度')