"""
    path: xiaoyi/BackEnd/app/api/site_config.py
    description: 网站设置、信息相关的路由、视图函数
"""

from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.deps.db import get_db
from app.schema.site_info import SiteInfoOut
from app.schema.response import ResponseModel
from app.crud.site_config import get_site_info

router = APIRouter(prefix="/site_config", tags=["网站设置管理"])


@router.get("/",
            response_model=ResponseModel[SiteInfoOut],
            summary='获取所有网站信息',
            description='无参数，获取数据库中关于博客网站的信息'
            )
async def site_config(db: Session = Depends(get_db)):
    data = get_site_info(db)
    result = {
        "code": 1,
        "message": "success",
        "data": data
    }
    return result
