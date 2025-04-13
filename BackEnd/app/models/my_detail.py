"""
    path: xiaoyi/BackEnd/app/models/my_detail.py
    description: 我的个人信息
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class MyDetail(Base):
    __tablename__ = 'my_detail'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='个人信息id')
    avatar: Mapped[str] = mapped_column(String(500), nullable=False, comment='我的头像')
    motto: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的座右铭')
    email: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的邮箱')
    wechat: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的微信')
    wechat_qr: Mapped[str] = mapped_column(String(500), nullable=True, comment="微信添加好友二维码")
    career: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的职业')
    city: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的城市')
    short_intro: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的简短介绍')
    full_intro: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的完整介绍')
    wisdom: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的智慧语句')
