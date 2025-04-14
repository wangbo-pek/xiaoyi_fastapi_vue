"""
    path: xiaoyi/BackEnd/schema/tag_category.py
    description: 笔记tag、category的Pydantic模型
"""

from pydantic import BaseModel, Field


class TagOut(BaseModel):
    name: str = Field(..., description='标签名')
    description: str = Field(..., description='标签描述')
    color: str = Field(..., description='标签颜色')

    class Config:
        from_attributes = True


class CategoryOut(BaseModel):
    name: str = Field(..., description='分类名')
    description: str = Field(..., description='分类描述')

    class Config:
        from_attributes = True