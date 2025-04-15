"""
    path: xiaoyi/BackEnd/schema/visitor.py
    description: 访客记录，轻量级日志
"""
from datetime import datetime
from pydantic import BaseModel, Field


class VisitorLogCreate(BaseModel):
    visitor_id: str = Field(..., description='访客唯一ID')
    path: str = Field(..., description='访问路径')
    referer: str = Field(..., description='来源页面')
    user_agent: str = Field(..., description='User-Agent')


class VisitorLogOut(BaseModel):
    id: int = Field(..., description='日志ID')
    visitor_id: str = Field(..., description='访客唯一ID')
    path: str = Field(..., description='访问路径')
    ip: str = Field(..., description='IP地址')
    visit_time:datetime = Field(..., description='访问时间')

    class Config:
        from_attributes = True

