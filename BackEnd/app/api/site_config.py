"""
    path: xiaoyi/BackEnd/app/api/site_config.py
    description: 网站设置、信息相关的路由、视图函数
"""

from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.deps.db import get_db
from app.schema.site_info import SiteInfoOut, SiteSocialLinkOut
from app.schema.response import ResponseModel
from app.crud.site_config import fetch_site_info_from_db, fetch_site_social_info_from_db

router = APIRouter(prefix="/site_config", tags=["网站设置管理"])


@router.get("/site_info",
            response_model=ResponseModel[SiteInfoOut],
            summary='获取网站所有信息',
            description='无参数，获取数据库中关于博客网站的信息'
            )
async def get_site_info(db: Session = Depends(get_db)):
    data = SiteInfoOut.model_validate(fetch_site_info_from_db(db))
    result = {
        "code": 1,
        "message": "success",
        "data": data
    }
    return result


@router.get("/site_social_info",
            response_model=ResponseModel[List[SiteSocialLinkOut]],
            summary='获取网站所有社交媒体前端数据',
            description='无参数，获取网站所有社交媒体前端数据'
            )
async def get_site_social_info(db:Session = Depends(get_db)):
    site_social_infos = fetch_site_social_info_from_db(db)
    data = []
    for site_social_info in site_social_infos:
        site_social_info = SiteSocialLinkOut.model_validate(site_social_info)
        data.append(site_social_info)
    result = {
        "code": 1,
        "message": "success",
        "data": data
    }
    return result