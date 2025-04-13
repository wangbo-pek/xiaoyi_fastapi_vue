"""
    path: xiaoyi/BackEnd/schema/diary.py
    description: 日记Diary的Pydantic模型
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class DiaryCreate(BaseModel):
    title: str = Field(..., description='日记标题')
    content: str = Field(..., description='日记正文')
    image_url: Optional[List[str]] = Field(default_factory=list, description="插图URL列表")


class DiaryListCreate(BaseModel):
    title: str = Field(..., description="日记标题")
    brief: str = Field(..., description="日记摘要")
    cover_img: str = Field(..., description="封面图URL")
    tags: List[str] = Field(default_factory=list, description="标签列表")