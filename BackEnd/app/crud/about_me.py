"""
    path: xiaoyi/BackEnd/crud/about_me.py
    description: about me的Diary的增删改查
"""
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.about_me import MyDetail, MyAbility, MySkill, MyTask, MyFavoriteLink

def fetch_detail_from_db(db:Session) -> MyDetail:
    stmt = select(MyDetail)
    return db.execute(stmt).scalar_one_or_none()


def fetch_ability_from_db(db:Session) -> list[MyAbility]:
    stmt = select(MyAbility)
    return list(db.execute(stmt).scalars().all())


def fetch_skill_from_db(db:Session) -> list[MySkill]:
    stmt = select(MySkill)
    return list(db.execute(stmt).scalars().all())


def fetch_task_from_db(db:Session) -> list[MyTask]:
    stmt = select(MyTask)
    return list(db.execute(stmt).scalars().all())


def fetch_favorite_link_from_db(db:Session) -> list[MyFavoriteLink]:
    stmt = select(MyFavoriteLink)
    return list(db.execute(stmt).scalars().all())