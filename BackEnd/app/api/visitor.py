"""
    path: xiaoyi/BackEnd/app/api/visitor.py
    description: 访客统计相关路由、视图函数
"""
from starlette.requests import Request

from BackEnd.app.crud.visitor import insert_visitor_log_to_db
from BackEnd.app.schema.visitor import VisitorLogOut, VisitorLogCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from BackEnd.app.deps.db import get_db
from BackEnd.app.schema.response import ResponseModel

router = APIRouter(prefix="/visitor", tags=["访客统计管理"])


@router.post("/log",
             response_model=ResponseModel[VisitorLogOut | None],
             summary='添加访客统计信息',
             description='前端有用户访问，则会向数据库插入访客信息'
             )
async def insert_visitor_log(log_info: VisitorLogCreate, request: Request, db: Session = Depends(get_db)):
    ip = request.headers.get("x-forwarded-for") or request.client.host
    raw_data = insert_visitor_log_to_db(db, log_info, ip)
    if raw_data is None:
        return {
            "code": 0,
            "message": "未添加访客信息",
            "data": None
        }
    data = VisitorLogOut.model_validate(raw_data)
    return {
        "code": 1,
        "message": "访客记录已保存",
        "data": data
    }
