# app/api/v1/test.py

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.deps.db import get_db

router = APIRouter(prefix="/test", tags=["测试"])


@router.get("/db")
def test_database_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))  # ✅ 使用 text() 包裹字符串 SQL
        return {"success": True, "message": "数据库连接成功！"}
    except Exception as e:
        return {"success": False, "error": str(e)}
