"""
    path: xiaoyi/BackEnd/app/api/v1/diary.py
    description: 日记相关路由、视图函数
"""

from fastapi import APIRouter

router = APIRouter(prefix="/diary", tags=["日记管理"])

@router.get("/diaries/")
async def diary_list():
    return None


@router.get("/diaries/{diary_id}/")
async def diary_detail():
    return None



