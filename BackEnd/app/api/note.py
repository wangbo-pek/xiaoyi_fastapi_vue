"""
    path: xiaoyi/BackEnd/app/api/note.py
    description: 文章相关路由、视图函数
"""

from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.deps.db import get_db
from app.schema.note import NoteListOut, NoteOut
from app.schema.response import ResponseModel
from app.crud.note import fetch_all_note_list_from_db, fetch_note_from_db

router = APIRouter(prefix="/note", tags=["文章管理"])


@router.get("/list",
            response_model=ResponseModel[List[NoteListOut]],
            summary='获取所有文章列表',
            description='无参数，获取数据库中所有NoteList'
            )
async def get_note_list(db: Session = Depends(get_db)):
    note_lists = fetch_all_note_list_from_db(db)
    data = []
    for note_list in note_lists:
        validated = NoteListOut.model_validate(note_list)
        data.append(validated)

    result = {
        "code": 1,
        "message": "success",
        "data": data
    }
    return result


@router.get("/")
async def get_notes():
    return None


@router.get("/{note_list_id}",
            response_model=ResponseModel[NoteOut],
            summary='获取note_list_id的文章主体',
            description='参数为note_list_id，int，获取数据库note_list_id所对应的文章主体'
            )
async def get_note_by_notelist_id(note_list_id: int, db: Session = Depends(get_db)):
    note = fetch_note_from_db(db, note_list_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    data = NoteOut.model_validate(note)
    return {
        "code": 1,
        "message": "success",
        "data": data
    }


@router.post("/{note_id}")
async def create_note():
    return None


@router.put("/")
async def update_note():
    return None


@router.delete("/")
async def delete_note():
    return None
