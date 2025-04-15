"""
    path: xiaoyi/BackEnd/schema/note.py
    description: 笔记Note的Pydantic模型
"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from app.schema.tag_category import TagOut, CategoryOut


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
    reading_time: int = Field(..., description='阅读时间')
    word_count: int = Field(..., description='字数')


class NoteListOut(BaseModel):
    id: int = Field(..., description='文章id', alias='noteListId')
    title: str = Field(..., description='文章标题')
    brief: str = Field(..., description='文章摘要')
    cover_img: str = Field(..., description='封面图url', alias='coverImg')
    slug: Optional[str] = Field(..., description='url别名')
    keyword: Optional[str] = Field(..., description='关键字')
    description: Optional[str] = Field(..., description='文章描述')
    category: CategoryOut = Field(..., description='文章分类')
    tags: List[TagOut] = Field(default_factory=list, description='文章的标签列表')

    is_pinned: bool = Field(..., description='是否被置顶', alias='isPinned')
    is_recommended: bool = Field(..., description='是否被推荐', alias='isRecommended')
    created_time: datetime = Field(..., description="创建时间", alias='createdTime')
    updated_time: datetime = Field(..., description="更新时间", alias='updatedTime')

    view_count: int = Field(..., description='浏览次数', alias='viewCount')
    like_count: int = Field(..., description="点赞次数", alias='likeCount')
    dislike_count: int = Field(..., description="被踩次数", alias='dislikeCount')
    reading_time: int = Field(..., description="阅读时间（单位：秒）", alias='readingTime')
    word_count: int = Field(..., description="文章字数", alias='wordCount')

    class Config:
        from_attributes = True
        validate_by_name = True


class NoteOut(BaseModel):
    title: str = Field(..., description='文章标题')
    content: str = Field(..., description='文章主体(markdown)', alias='markdownContent')
    image_url: List[str] = Field(default=None, description='文章插图', alias='imageUrls')

    class Config:
        from_attributes = True
        validate_by_name = True


class UpdateNoteStatisticIn(BaseModel):
    noteListId: int
    action: str


class UpdateNoteStatisticOut(BaseModel):
    result: str
