"""
    path: xiaoyi/BackEnd/schema/note.py
    description: 笔记Note的Pydantic模型
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    title: str = Field(..., description='文章标题')
    content: str = Field(..., description='文章正文')
    image_url: Optional[List[str]] = Field(default_factory=list, description="插图URL列表")


class NoteListCreate(BaseModel):
    title: str = Field(..., description="文章标题")
    brief: str = Field(..., description="文章摘要")
    cover_img: str = Field(..., description="封面图 URL")
    category: str = Field(..., description="分类名称")
    tags: List[str] = Field(default_factory=list, description="标签列表")
