"""
    path: xiaoyi/BackEnd/app/api/note.py
    description: 文章相关路由、视图函数
"""

from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from BackEnd.app.deps.db import get_db
from BackEnd.app.schema.note import NoteListOut, NoteOut, UpdateNoteStatisticIn, UpdateNoteStatisticOut
from BackEnd.app.schema.response import ResponseModel
from BackEnd.app.crud.note import fetch_all_note_list_from_db, fetch_note_from_db, update_note_statistic_from_db

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
            summary='获取笔记内容',
            description='参数为note_list_id(int)，根据id获取笔记内容'
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


@router.patch("/update_note_statistic",
              response_model=ResponseModel[UpdateNoteStatisticOut],
              summary='更新note的统计信息',
              description='根据参数id选择更新哪一篇Note，根据action，选择更新什么字段'
              )
async def update_note_statistic(update_info: UpdateNoteStatisticIn, db:Session=Depends(get_db)):
    data = update_note_statistic_from_db(db, update_info)
    data = UpdateNoteStatisticOut.model_validate(data)
    return {
        "code": 1,
        "message": "success",
        "data": data
    }
