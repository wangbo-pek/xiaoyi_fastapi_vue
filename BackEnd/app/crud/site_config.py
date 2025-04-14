"""
    path: xiaoyi/BackEnd/crud/site_config.py
    description: 数据库中，网站信息配置的增删改查
"""

from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.site_info import SiteInfo
from app.schema.site_info import SiteInfoOut

def get_site_info(db: Session) -> SiteInfoOut:
    stmt = select(SiteInfo)
    site_info = db.execute(stmt).scalar_one_or_none()
    site_info = SiteInfoOut.model_validate(site_info)
    return site_info