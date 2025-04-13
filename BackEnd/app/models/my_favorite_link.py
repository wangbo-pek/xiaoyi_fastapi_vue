"""
    path: xiaoyi/BackEnd/app/models/my_favorite_link.py
    description: 我的个人信息
"""

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class MyFavoriteLink(Base):
    __tablename__ = 'my_favorite_link'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='收藏文章id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='收藏文章标题')
    url: Mapped[str] = mapped_column(String(500), nullable=False, comment='收藏文章url')
    favicon_url: Mapped[str] = mapped_column(String(500), nullable=False, comment='收藏文章网站icon url')
    is_out_of_wall: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='是否墙外')
