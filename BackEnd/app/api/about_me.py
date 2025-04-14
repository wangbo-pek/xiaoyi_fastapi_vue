"""
    path: xiaoyi/BackEnd/app/api/about_me.py
    description: about me的路由、视图函数
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.about_me import *
from app.deps.db import get_db
from app.schema.response import ResponseModel
from app.schema.about_me import *


router = APIRouter(prefix="/about_me", tags=["博客网站我的信息"])

@router.get("/my_detail",
            response_model=ResponseModel[MyDetailOut],
            summary='获取my_detail信息',
            description='无参数，获取my_detail信息'
            )
async def get_detail(db: Session = Depends(get_db)):
    data = get_detail_from_db(db)
    result = {
        "code": 1,
        "message": "success",
        "data": data
    }
    return result


@router.get('/my_ability',
            response_model=ResponseModel[list[MyAbilityOut]],
            summary='获取my_ability信息',
            description='无参数，获取my_ability信息'
            )
async def get_ability(db:Session = Depends(get_db)):
    data = get_ability_from_db(db)
    result = {
        "code":1,
        "message":"success",
        "data":data
    }
    return result


@router.get('/my_skill',
            response_model=ResponseModel[list[MySkillOut]],
            summary='获取my_skill信息',
            description='无参数，获取my_skill信息'
            )
async def get_skill(db:Session = Depends(get_db)):
    data = get_skill_from_db(db)
    result = {
        "code":1,
        "message":"success",
        "data":data
    }
    return result


@router.get('/my_task',
            response_model=ResponseModel[list[MyTaskOut]],
            summary='获取my_task信息',
            description='无参数，获取my_task信息'
            )
async def get_task(db:Session = Depends(get_db)):
    data = get_task_from_db(db)
    result = {
        "code":1,
        "message":"success",
        "data":data
    }
    return result


@router.get('/my_favorite_link',
            response_model=ResponseModel[list[MyFavoriteLinkOut]],
            summary='获取my_favorite_link信息',
            description='无参数，获取my_favorite_link信息'
            )
async def get_favorite_link(db:Session = Depends(get_db)):
    data = get_favorite_link_from_db(db)
    result = {
        "code":1,
        "message":"success",
        "data":data
    }
    return result