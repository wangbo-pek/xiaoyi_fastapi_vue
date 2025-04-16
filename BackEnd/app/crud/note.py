"""
    path: xiaoyi/BackEnd/crud/note.py
    description: 数据库中，笔记Note的增删改查
"""
from fastapi import HTTPException
from sqlalchemy import select, update
from sqlalchemy.orm import Session, joinedload
from BackEnd.app.models import Category, Tag,NoteList, Note
from BackEnd.app.schema.note import NoteCreate, NoteListCreate, UpdateNoteStatisticIn, UpdateNoteStatisticOut


def create_note_and_list(
        db: Session,
        note_data: NoteCreate,
        note_list_data: NoteListCreate
) -> Note:
    # 获取category对象
    stmt = select(Category).where(Category.name == note_list_data.category)
    category_obj = db.execute(stmt).scalar_one_or_none()
    if not category_obj:
        raise ValueError(f'分类不存在：{note_list_data.category}')

    # 迭代tags，如果数据库中有则跳过，没有则创建新tag
    tag_objs = []
    for tag_name in note_list_data.tags:
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

    note_list = NoteList(
        title=note_list_data.title,
        brief=note_list_data.brief,
        cover_img=note_list_data.cover_img,
        category=category_obj,
        word_count=note_list_data.word_count,
        reading_time=note_list_data.reading_time,
        tags=tag_objs
    )

    db.add(note_list)
    db.flush()

    note = Note(
        title=note_data.title,
        content=note_data.content,
        image_url=note_data.image_url,
        note_list=note_list
    )

    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def fetch_all_note_list_from_db(db: Session) -> list[NoteList]:
    # 获取满足条件的NoteList
    stmt = (
        select(NoteList)
        .join(NoteList.category)
        .options(
            joinedload(NoteList.category),
            joinedload(NoteList.tags)
        )
        .where(
            NoteList.is_show == True,
            NoteList.is_deleted == False,
            Category.is_show == True,
            Category.is_deleted == False
        )
    )

    note_lists = db.execute(stmt).unique().scalars().all()

    for note_list in note_lists:
        valid_tags = []
        for tag in note_list.tags:
            if tag.is_show and not tag.is_deleted:
                valid_tags.append(tag)
        note_list.tags = valid_tags

    return list(note_lists)


def fetch_note_from_db(db: Session, note_list_id: int) -> Note:
    stmt = select(Note).where(Note.note_list_id == note_list_id)
    return db.execute(stmt).scalar_one_or_none()


def update_note_statistic_from_db(db: Session, update_info: UpdateNoteStatisticIn):
    stmt = update(NoteList).where(NoteList.id == update_info.noteListId)

    if update_info.action == 'like':
        stmt = stmt.values(like_count=NoteList.like_count + 1)
    elif update_info.action == 'dislike':
        stmt = stmt.values(dislike_count=NoteList.dislike_count + 1)
    elif update_info.action == 'undoLike':
        stmt = stmt.values(like_count=NoteList.like_count - 1)
    elif update_info.action == 'undoDislike':
        stmt = stmt.values(dislike_count=NoteList.dislike_count - 1)
    elif update_info.action == 'view':
        stmt = stmt.values(view_count=NoteList.view_count + 1)
    else:
        raise HTTPException(status_code=400, detail="Invalid Action")

    db.execute(stmt)
    db.commit()
    return {"result":"OK"}
