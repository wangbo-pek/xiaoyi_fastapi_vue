"""
    path: xiaoyi/BackEnd/crud/note.py
    description: 数据库中，笔记Note的增删改查
"""

from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Category, Tag
from app.models.note import Note
from app.models.note_list import NoteList
from app.schema.note import NoteCreate, NoteListCreate


def create_note_and_list(
        db:Session,
        note_data:NoteCreate,
        note_list_data:NoteListCreate
) -> Note:
    # 获取category对象
    stmt = select(Category).where(Category.name==note_list_data.category)
    category_obj = db.execute(stmt).scalar_one_or_none()
    if not category_obj:
        raise ValueError(f'分类不存在：{note_list_data.category}')

    # 迭代tags，如果数据库中有则跳过，没有则创建新tag
    tag_objs = []
    for tag_name in note_list_data.tags:
        stmt = select(Tag).where(Tag.name==tag_name)
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

