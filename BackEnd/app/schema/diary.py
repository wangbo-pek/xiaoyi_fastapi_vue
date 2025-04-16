"""
    path: xiaoyi/BackEnd/schema/diary.py
    description: 日记Diary的Pydantic模型
"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.schema.tag_category import TagOut


class DiaryCreate(BaseModel):
    title: str = Field(..., description='日记标题')
    content: str = Field(..., description='日记正文')
    image_url: Optional[List[str]] = Field(default_factory=list, description="插图URL列表")


class DiaryListCreate(BaseModel):
    title: str = Field(..., description="日记标题")
    brief: str = Field(..., description="日记摘要")
    cover_img: str = Field(..., description="封面图URL")
    tags: List[str] = Field(default_factory=list, description="标签列表")
    reading_time: int = Field(..., description='阅读时间')
    word_count: int = Field(..., description='字数')


class DiaryListOut(BaseModel):
    id: int = Field(..., description='日记id', alias='diaryListId')
    title: str = Field(..., description='日记标题')
    brief: str = Field(..., description='日记摘要')
    cover_img: str = Field(..., description='封面图url', alias='coverImg')
    tags: List[TagOut] = Field(default_factory=list, description='日记的标签列表')

    created_time: datetime = Field(..., description="创建时间", alias='createdTime')
    updated_time: datetime = Field(..., description="更新时间", alias='updatedTime')

    view_count: int = Field(..., description='浏览次数', alias='viewCount')
    reading_time: int = Field(..., description="阅读时间（单位：秒）", alias='readingTime')
    word_count: int = Field(..., description="日记字数", alias='wordCount')

    class Config:
        from_attributes = True
        validate_by_name = True


class DiaryOut(BaseModel):
    title: str = Field(..., description='日记标题')
    content: str = Field(..., description='日记主体(markdown)', alias='markdownContent')
    image_url: List[str] = Field(default=None, description='日记插图', alias='imageUrls')

    class Config:
        from_attributes = True
        validate_by_name = True


class UpdateDiaryStatisticIn(BaseModel):
    diaryListId: int
    action: str


class UpdateDiaryStatisticOut(BaseModel):
    result: str