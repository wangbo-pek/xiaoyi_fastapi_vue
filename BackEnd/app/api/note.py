"""
    path: xiaoyi/BackEnd/app/api/note.py
    description: 文章相关路由、视图函数
"""

from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.deps.db import get_db
from app.schema.note import NoteListOut
from app.schema.response import ResponseModel
from app.crud.note import get_all_note_list

router = APIRouter(prefix="/notes", tags=["文章管理"])


@router.get("/list",
            response_model=ResponseModel[List[NoteListOut]],
            summary='获取所有文章列表',
            description='无参数，获取数据库中所有NoteList'
            )
async def get_note_list(db: Session = Depends(get_db)):
    data = get_all_note_list(db)
    result = {
        "code": 1,
        "message": "success",
        "data": data
    }
    return result


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
