"""
    path: xiaoyi/BackEnd/app/api/tag_category.py
    description: 标签、分类路由、视图函数
"""

from fastapi import APIRouter

router = APIRouter(prefix="/tag_category", tags=["标签分类管理"])

@router.get("/")
async def tag_category():
    return None