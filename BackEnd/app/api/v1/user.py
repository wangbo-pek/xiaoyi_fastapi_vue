"""
    path: xiaoyi/BackEnd/app/api/v1/user.py
    description: 后台管理用户的路由、视图函数
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["后台用户管理"])

@router.get("/")
async def user():
    return None