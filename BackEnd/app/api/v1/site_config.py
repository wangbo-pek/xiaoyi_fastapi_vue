"""
    path: xiaoyi/BackEnd/app/api/v1/site_config.py
    description: 网站设置、信息相关的路由、视图函数
"""

from fastapi import APIRouter

router = APIRouter(prefix="/site_config", tags=["网站设置管理"])

@router.get("/")
async def site_config():
    return None