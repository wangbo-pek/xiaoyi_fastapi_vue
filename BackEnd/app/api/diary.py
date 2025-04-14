"""
    path: xiaoyi/BackEnd/app/api/diary.py
    description: 日记相关路由、视图函数
"""
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.diary import fetch_all_diary_list_from_db
from app.deps.db import get_db
from app.schema.diary import DiaryListOut
from app.schema.response import ResponseModel

router = APIRouter(prefix="/diary", tags=["日记管理"])


@router.get("/list",
            response_model=ResponseModel[List[DiaryListOut]],
            summary='获取所有文章列表',
            description='无参数，获取数据库中所有NoteList'
            )
async def get_diary_list(db: Session = Depends(get_db)):
    diary_lists = fetch_all_diary_list_from_db(db)
    data = []
    for diary_list in diary_lists:
        validated = DiaryListOut.model_validate(diary_list)
        data.append(validated)
    result = {
        "code": 1,
        "message": "success",
        "data": data
    }
    return result


@router.get("/")
async def get_diaries():
    return None


@router.get("/{note_id}/")
async def get_diary():
    return None


@router.post("/{note_id}")
async def create_diary():
    return None


@router.put("/")
async def update_diary():
    return None


@router.delete("/")
async def delete_diary():
    return None
