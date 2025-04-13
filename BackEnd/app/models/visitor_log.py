"""
    path: xiaoyi/BackEnd/app/models/visitor_log.py
    description: 访客日志
"""

from datetime import datetime
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class VisitorLog(Base):
    __tablename__ = "visitor_log"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment="日志 ID")
    ip: Mapped[str] = mapped_column(String(64), nullable=False, comment="IP 地址")
    user_agent: Mapped[str] = mapped_column(String(512), nullable=True, comment="User-Agent")
    browser: Mapped[str] = mapped_column(String(64), nullable=True, comment="浏览器")
    os: Mapped[str] = mapped_column(String(64), nullable=True, comment="操作系统")
    device: Mapped[str] = mapped_column(String(64), nullable=True, comment="设备类型")

    country: Mapped[str] = mapped_column(String(64), nullable=True, comment="国家")
    province: Mapped[str] = mapped_column(String(64), nullable=True, comment="省份")
    city: Mapped[str] = mapped_column(String(64), nullable=True, comment="城市")

    referer: Mapped[str] = mapped_column(String(300), nullable=True, comment="来源页面")
    path: Mapped[str] = mapped_column(String(300), nullable=False, comment="访问路径")
    query: Mapped[str] = mapped_column(String(300), nullable=True, comment="URL 查询参数")
    method: Mapped[str] = mapped_column(String(10), nullable=False, comment="请求方法")
    status_code: Mapped[int] = mapped_column(Integer, nullable=False, comment="响应状态码")

    visit_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False, comment="访问时间")
