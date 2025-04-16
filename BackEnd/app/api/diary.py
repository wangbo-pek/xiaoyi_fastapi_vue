"""
    path: xiaoyi/BackEnd/app/api/diary.py
    description: 日记相关路由、视图函数
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from BackEnd.app.crud.diary import fetch_all_diary_list_from_db, fetch_diary_from_db, update_diary_statistic_from_db
from BackEnd.app.deps.db import get_db
from BackEnd.app.schema.diary import DiaryListOut, DiaryOut, UpdateDiaryStatisticIn, UpdateDiaryStatisticOut
from BackEnd.app.schema.response import ResponseModel

router = APIRouter(prefix="/diary", tags=["日记管理"])


@router.get("/list",
            response_model=ResponseModel[List[DiaryListOut]],
            summary='获取所有日记列表',
            description='无参数，获取数据库中所有DiaryList'
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


@router.get("/{diary_list_id}",
            response_model=ResponseModel[DiaryOut],
            summary='获取日记内容',
            description='参数为diary_list_id(int)，根据id获取日记内容')
async def get_diary_by_notelist_id(diary_list_id: int, db: Session = Depends(get_db)):
    diary = fetch_diary_from_db(db, diary_list_id)
    if not diary:
        raise HTTPException(status_code=404, detail="Note not found")
    data = DiaryOut.model_validate(diary)
    return {
        "code": 1,
        "message": "success",
        "data": data
    }


@router.post("/{note_id}")
async def create_diary():
    return None


@router.put("/")
async def update_diary():
    return None


@router.delete("/")
async def delete_diary():
    return None


@router.patch("/update_diary_statistic",
              response_model=ResponseModel[UpdateDiaryStatisticOut],
              summary='更新diary的view_count',
              description='根据参数id选择更新哪一篇Diary需要更新view_count'
              )
async def update_diary_statistic(update_info: UpdateDiaryStatisticIn, db:Session=Depends(get_db)):
    data = update_diary_statistic_from_db(db, update_info)
    data = UpdateDiaryStatisticOut.model_validate(data)
    return {
        "code": 1,
        "message": "success",
        "data": data
    }