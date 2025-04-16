"""
    path: xiaoyi/BackEnd/app/models/visitor_log.py
    description: 访客日志
"""

from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from BackEnd.app.core.database import Base


class VisitorLog(Base):
    __tablename__ = "visitor_log"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment="日志ID")
    visitor_id: Mapped[str] = mapped_column(String(64), index=True, comment="访客唯一ID(如localStorage中的UUID)")
    ip: Mapped[str] = mapped_column(String(64), comment="IP地址")
    path: Mapped[str] = mapped_column(String(512), comment="访问路径")
    referer: Mapped[str] = mapped_column(String(512), nullable=True, comment="来源页面")
    user_agent: Mapped[str] = mapped_column(String(1024), nullable=True, comment="User-Agent")
    visit_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), comment="访问时间")

