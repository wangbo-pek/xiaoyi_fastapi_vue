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


class TagWithCountOut(BaseModel):
    name: str = Field(..., description='标签名')
    description: str = Field(..., description='标签描述')
    color: str = Field(..., description='标签颜色')
    tag_count: int = Field(..., description='标签下article数量', alias='tagCount')

    class Config:
        from_attributes = True
        validate_by_name = True


class CategoryWithCountOut(BaseModel):
    name: str = Field(..., description='分类名')
    description: str = Field(..., description='分类描述')
    category_count: int = Field(..., description='分类下note数量', alias='categoryCount')

    class Config:
        from_attributes = True
        validate_by_name = True