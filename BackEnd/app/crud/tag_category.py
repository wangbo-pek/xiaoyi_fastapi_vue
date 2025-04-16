"""
    path: xiaoyi/BackEnd/crud/tag_category.py
    description: 数据库中，标签和分类的增删改查
"""

from sqlalchemy import select, func
from sqlalchemy.orm import Session
from app.models import note_tag, Tag, Category
from app.models.association import diary_tag


def fetch_tags_with_count_from_db(db: Session) -> list[Tag]:
    # 分类下note数量
    note_stmt = (
        select(
            Tag.id.label('tag_id'),
            func.count(note_tag.c.note_list_id).label('note_count')
        )
        .select_from(note_tag)
        .join(Tag, Tag.id == note_tag.c.tag_id)
        .group_by(Tag.id)
        .order_by(Tag.id)
        .subquery()
    )

    # Diary 数量
    diary_stmt = (
        select(
            Tag.id.label("tag_id"),
            func.count(diary_tag.c.diary_list_id).label("diary_count")
        )
        .select_from(diary_tag)
        .join(Tag, Tag.id == diary_tag.c.tag_id)
        .group_by(Tag.id)
        .subquery()
    )

    # 聚合 Tag + note_count + diary_count
    stmt = (
        select(
            Tag.id,
            Tag.name,
            Tag.description,
            Tag.color,
            func.coalesce(note_stmt.c.note_count, 0),
            func.coalesce(diary_stmt.c.diary_count, 0)
        )
        .outerjoin(note_stmt, note_stmt.c.tag_id == Tag.id)
        .outerjoin(diary_stmt, diary_stmt.c.tag_id == Tag.id)
        .where(Tag.is_show == True, Tag.is_deleted == False)
        .order_by(Tag.id)
    )

    result_from_db = db.execute(stmt).all()
    result = []
    for id_, name, description, color, note_count, diary_count in result_from_db:
        result.append({
            'name': name,
            'description': description,
            'color': color,
            'tag_count': note_count + diary_count
        })
    return result


def fetch_categories_with_count_from_db(db: Session):
    stmt = (
        select(
            Category.name,
            Category.description,
            func.count(NoteList.id).label('note_count')
        )
        .outerjoin(NoteList, NoteList.category_id == Category.id)
        .where(Category.is_show == True, Category.is_deleted == False)
        .group_by(Category.id)
        .order_by(Category.id)
    )
    result_from_db = db.execute(stmt).all()
    result = []
    for name, description, category_count in result_from_db:
        result.append({
            'name': name,
            'description': description,
            'category_count': category_count
        })
    return result
