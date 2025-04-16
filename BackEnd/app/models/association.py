"""
    path: xiaoyi/BackEnd/app/models/association.py
    description: 定义多对多模型的中间表
"""

from sqlalchemy import Column, Table, ForeignKey
from BackEnd.app.core.database import Base


# note_list和tag的中间表
note_tag = Table(
    'notelist_tag',
    Base.metadata,
    Column('note_list_id', ForeignKey('note_list.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True),
)

# diary_list和tag的中间表
diary_tag = Table(
    'diarylist_tag',
    Base.metadata,
    Column('diary_list_id', ForeignKey('diary_list.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True),
)