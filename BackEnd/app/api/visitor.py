"""
    path: xiaoyi/BackEnd/app/api/visitor.py
    description: 访客统计相关路由、视图函数
"""

from fastapi import APIRouter

router = APIRouter(prefix="/visitor", tags=["访客统计管理"])

@router.get("/")
async def visitor():
    return None