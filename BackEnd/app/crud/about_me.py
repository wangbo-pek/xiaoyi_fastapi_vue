"""
    path: xiaoyi/BackEnd/crud/about_me.py
    description: about me的Diary的增删改查
"""
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.about_me import MyDetail, MyAbility, MySkill, MyTask, MyFavoriteLink
from app.schema.about_me import MyDetailOut, MyAbilityOut, MySkillOut, MyTaskOut, MyFavoriteLinkOut

def get_detail_from_db(db:Session) -> MyDetailOut:
    stmt = select(MyDetail)
    my_detail = db.execute(stmt).scalar_one_or_none()
    my_detail = MyDetailOut.model_validate(my_detail)
    return my_detail


def get_ability_from_db(db:Session) -> list[MyAbilityOut]:
    stmt = select(MyAbility)
    my_abilities = db.execute(stmt).scalars().all()
    my_ability_list = []
    for my_ability in my_abilities:
        my_ability = MyAbilityOut.model_validate(my_ability)
        my_ability_list.append(my_ability)
    return my_ability_list


def get_skill_from_db(db:Session) -> list[MySkillOut]:
    stmt = select(MySkill)
    my_skills = db.execute(stmt).scalars().all()
    my_skill_list = []
    for my_skill in my_skills:
        my_skill = MySkillOut.model_validate(my_skill)
        my_skill_list.append(my_skill)
    return my_skill_list


def get_task_from_db(db:Session) -> list[MyTaskOut]:
    stmt = select(MyTask)
    my_tasks = db.execute(stmt).scalars().all()
    my_task_list = []
    for my_task in my_tasks:
        my_task = MyTaskOut.model_validate(my_task)
        my_task_list.append(my_task)
    return my_task_list


def get_favorite_link_from_db(db:Session) -> list[MyFavoriteLinkOut]:
    stmt = select(MyFavoriteLink)
    my_favorite_links = db.execute(stmt).scalars().all()
    my_favorite_link_list = []
    for my_favorite_link in my_favorite_links:
        my_favorite_link = MyFavoriteLinkOut.model_validate(my_favorite_link)
        my_favorite_link_list.append(my_favorite_link)
    return my_favorite_link_list