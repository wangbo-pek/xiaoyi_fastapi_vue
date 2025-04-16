"""
    path: xiaoyi/BackEnd/app/models/site_social_link.py
    description: 网站相关信息
"""

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from BackEnd.app.core.database import Base


class SiteSocialLink(Base):
    __tablename__ = 'site_social_link'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='社交媒体id')
    name: Mapped[str] = mapped_column(String(100), nullable=False, comment='社交媒体名称')
    url: Mapped[str] = mapped_column(String(500), nullable=False, comment='社交媒体url')
    favicon_url: Mapped[str] = mapped_column(String(500), nullable=False, comment='社交媒体icon url')
