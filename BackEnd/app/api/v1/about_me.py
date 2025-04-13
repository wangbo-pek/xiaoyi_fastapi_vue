"""
    path: xiaoyi/BackEnd/app/api/v1/about_me.py
    description: 关于我 路由、视图函数
"""

from fastapi import APIRouter

router = APIRouter(prefix="/about_me", tags=["博客网站我的信息"])

@router.get("/")
async def about_me():
    return None