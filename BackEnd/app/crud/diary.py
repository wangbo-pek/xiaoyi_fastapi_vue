"""
    path: xiaoyi/BackEnd/crud/diary.py
    description: 数据库中，日记Diary的增删改查
"""

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from app.models import Tag
from app.models.diary import Diary
from app.models.diary_list import DiaryList
from app.schema.diary import DiaryCreate, DiaryListCreate, DiaryListOut


def create_diary_and_list(
        db: Session,
        diary_data: DiaryCreate,
        diary_list_data: DiaryListCreate
) -> Diary:
    # 迭代tags，如果数据库中有则跳过，没有则创建新tag
    tag_objs = []
    for tag_name in diary_list_data.tags:
        stmt = select(Tag).where(Tag.name == tag_name)
        tag = db.execute(stmt).scalar_one_or_none()
        if not tag:
            tag = Tag(
                name=tag_name,
                description='自动添加',
                color='#2196f3'
            )
            db.add(tag)
            db.flush()
        tag_objs.append(tag)

    diary_list = DiaryList(
        title=diary_list_data.title,
        brief=diary_list_data.brief,
        cover_img=diary_list_data.cover_img,
        tags=tag_objs
    )

    db.add(diary_list)
    db.flush()

    diary = Diary(
        title=diary_data.title,
        content=diary_data.content,
        image_url=diary_data.image_url,
        diary_list=diary_list
    )

    db.add(diary)
    db.commit()
    db.refresh(diary)
    return diary


def get_all_diary_list(db:Session) -> list[DiaryListOut]:
    # 获取满足条件的DiaryList
    stmt = (
        select(DiaryList)
        .options(joinedload(DiaryList.tags))
    ).where(
        DiaryList.is_show == True,
        DiaryList.is_deleted == False
    )

    diary_lists = db.execute(stmt).unique().scalars().all()
    result = []

    for diary_list in diary_lists:
        valid_tags = []
        for tag in diary_list.tags:
            if tag.is_show and not tag.is_deleted:
                valid_tags.append(tag)

        diary_list.tags = valid_tags
        item = DiaryListOut.model_validate(diary_list)
        result.append(item)
    return result


