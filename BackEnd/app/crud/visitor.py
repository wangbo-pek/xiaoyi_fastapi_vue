"""
    path: xiaoyi/BackEnd/crud/visitor.py
    description: 访客信息的增删改查
"""
from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session
from BackEnd.app.models import VisitorLog
from BackEnd.app.schema.visitor import VisitorLogCreate


def insert_visitor_log_to_db(db: Session, log_info: VisitorLogCreate, ip: str) -> VisitorLog|None:
    time_threshold = datetime.now() - timedelta(seconds=60)

    # 查询是否60秒内有记录
    stmt = (
        select(VisitorLog)
        .where(VisitorLog.visitor_id==log_info.visitor_id)
        .where(VisitorLog.path==log_info.path)
        .where(VisitorLog.visit_time >= time_threshold)
    )

    result = db.execute(stmt).scalar_one_or_none()

    if result is not None:
        return None

    # 插入新纪录
    new_log = VisitorLog(
        visitor_id=log_info.visitor_id,
        ip=ip,
        path=log_info.path,
        referer=log_info.referer,
        user_agent=log_info.user_agent,
        visit_time=datetime.now()
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log
