"""
    path: xiaoyi/BackEnd/crud/diary.py
    description: 数据库中，日记Diary的增删改查
"""
from fastapi import HTTPException
from sqlalchemy import select, update
from sqlalchemy.orm import Session, joinedload
from app.models import Tag
from app.models.diary import Diary
from app.models.diary_list import DiaryList
from app.schema.diary import DiaryCreate, DiaryListCreate, UpdateDiaryStatisticIn


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
        word_count=diary_list_data.word_count,
        reading_time=diary_list_data.reading_time,
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


def fetch_all_diary_list_from_db(db:Session) -> list[DiaryList]:
    # 获取满足条件的DiaryList
    stmt = (
        select(DiaryList)
        .options(joinedload(DiaryList.tags))
    ).where(
        DiaryList.is_show == True,
        DiaryList.is_deleted == False
    )

    diary_lists = db.execute(stmt).unique().scalars().all()

    for diary_list in diary_lists:
        valid_tags = []
        for tag in diary_list.tags:
            if tag.is_show and not tag.is_deleted:
                valid_tags.append(tag)

        diary_list.tags = valid_tags
    return list(diary_lists)


def fetch_diary_from_db(db:Session, diary_list_id:int) -> Diary:
    stmt = select(Diary).where(Diary.diary_list_id == diary_list_id)
    return db.execute(stmt).scalar_one_or_none()


def update_diary_statistic_from_db(db: Session, update_info: UpdateDiaryStatisticIn):
    stmt = update(DiaryList).where(DiaryList.id == update_info.diaryListId)

    if update_info.action == 'view':
        stmt = stmt.values(view_count=DiaryList.view_count + 1)
    else:
        raise HTTPException(status_code=400, detail="Invalid Action")

    db.execute(stmt)
    db.commit()
    return {"result":"OK"}