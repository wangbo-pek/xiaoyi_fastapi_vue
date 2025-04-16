"""
    path: xiaoyi/BackEnd/crud/site_config.py
    description: 数据库中，网站信息配置的增删改查
"""

from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import SiteInfo, SiteSocialLink


def fetch_site_info_from_db(db: Session) -> SiteInfo:
    stmt = select(SiteInfo)
    return db.execute(stmt).scalar_one_or_none()


def fetch_site_social_info_from_db(db: Session) -> list[SiteSocialLink]:
    stmt = select(SiteSocialLink)
    return db.execute(stmt).scalars().all()