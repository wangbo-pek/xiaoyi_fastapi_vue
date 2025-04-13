"""
    path: xiaoyi/BackEnd/app/api/v1/note.py
    description: 文章相关路由、视图函数
"""

from fastapi import APIRouter

router = APIRouter(prefix="/notes", tags=["文章管理"])


@router.get("/list")
async def get_note_list():
    return None


@router.get("/")
async def get_notes():
    return None


@router.get("/{note_id}/")
async def get_note():
    return None


@router.post("/{note_id}")
async def create_note():
    return None


@router.put("/")
async def update_note():
    return None


@router.delete("/")
async def delete_note():
    return None
