"""
    path: xiaoyi/BackEnd/app/api/tag_category.py
    description: 标签、分类路由、视图函数
"""
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.deps.db import get_db
from app.schema.response import ResponseModel
from app.schema.tag_category import TagWithCountOut, CategoryWithCountOut
from app.crud.tag_category import *

router = APIRouter(prefix="/tag_category", tags=["标签分类管理"])


@router.get("/tags",
            response_model=ResponseModel[List[TagWithCountOut]],
            summary='获取所有标签',
            description='无参数，获取数据库中所有标签'
            )
async def tag_category(db: Session = Depends(get_db)):
    tags = fetch_tags_with_count_from_db(db)
    data = []
    for tag in tags:
        tag = TagWithCountOut.model_validate(tag)
        data.append(tag)
    return {
        "code": 1,
        "message": "success",
        "data": data
    }


@router.get("/categories",
            response_model=ResponseModel[List[CategoryWithCountOut]],
            summary='获取所有分类',
            description='无参数，获取数据库中所有分类'
            )
async def tag_category(db: Session = Depends(get_db)):
    categories = fetch_categories_with_count_from_db(db)
    data = []
    for category in categories:
        category = CategoryWithCountOut.model_validate(category)
        data.append(category)
    return {
        "code": 1,
        "message": "success",
        "data": data
    }
