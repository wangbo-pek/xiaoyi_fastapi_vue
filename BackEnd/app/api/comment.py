"""
    path: xiaoyi/BackEnd/app/api/comment.py
    description: 评论路由、视图函数
"""

from fastapi import APIRouter

router = APIRouter(prefix="/comment", tags=["评论管理"])

@router.get("/")
async def comment():
    return None