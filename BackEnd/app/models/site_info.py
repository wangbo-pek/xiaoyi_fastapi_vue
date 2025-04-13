"""
    path: xiaoyi/BackEnd/app/models/site_info.py
    description: 网站相关信息
"""

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.core.database import Base

class SiteInfo(Base):
    __tablename__ = "site_info"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment="站点信息唯一ID")
    site_name: Mapped[str] = mapped_column(String(100), nullable=False, comment="网站名称")
    site_subtitle: Mapped[str] = mapped_column(String(200), nullable=True, comment="网站副标题")

    logo_url: Mapped[str] = mapped_column(String(500), nullable=True, comment="Logo 地址")
    favicon_url: Mapped[str] = mapped_column(String(500), nullable=True, comment="Favicon 图标地址")

    icp_number: Mapped[str] = mapped_column(String(100), nullable=True, comment="ICP备案号")
    public_security: Mapped[str] = mapped_column(String(100), nullable=True, comment="公网安备案号")

    github_url: Mapped[str] = mapped_column(String(300), nullable=True, comment="GitHub 地址")

    keywords: Mapped[str] = mapped_column(String(300), nullable=True, comment="SEO 关键词")
    description: Mapped[str] = mapped_column(String(500), nullable=True, comment="SEO 描述")

    created_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False, comment="创建时间")
    updated_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False, comment="更新时间")

    wechat_sponsor_qr: Mapped[str] = mapped_column(String(500), nullable=True, comment="微信收款二维码地址")
    alipay_sponsor_qr: Mapped[str] = mapped_column(String(500), nullable=True, comment="支付宝收款二维码地址")
