"""
    path: xiaoyi/BackEnd/app/models/about_me.py
    description: 我的个人信息：my_detail、my_skill、my_ability、my_task、my_favorite_link
"""
from datetime import datetime

from pydantic import BaseModel, Field


class MyDetailOut(BaseModel):
    name: str = Field(..., description='名字')
    nickname: str = Field(..., description='昵称')
    avatar: str = Field(..., description='我的头像')
    motto: str = Field(..., description='我的座右铭')
    email: str = Field(..., description='我的邮箱')
    wechat: str = Field(..., description='我的微信')
    wechat_qr: str = Field(..., description='微信添加好友二维码', alias='wechatQR')
    city: str = Field(..., description='我的城市')
    short_intro: str = Field(..., description='我的简短介绍', alias='shortIntro')
    full_intro: str = Field(..., description='我的完整介绍', alias='fullIntro')
    wisdom: str = Field(..., description='我的智慧语句')

    class Config:
        from_attributes = True
        validate_by_name = True


class MyAbilityOut(BaseModel):
    title: str = Field(..., description='我的能力维度')
    description: str = Field(..., description='能力描述')
    degree: int = Field(..., description='掌握程度')

    class Config:
        from_attributes = True
        validate_by_name = True


class MySkillOut(BaseModel):
    title: str = Field(..., description='我的技能维度')
    description: str = Field(..., description='技能描述')
    degree: int = Field(..., description='掌握程度')

    class Config:
        from_attributes = True
        validate_by_name = True


class MyTaskOut(BaseModel):
    title: str = Field(..., description='我的任务名称')
    status: int = Field(..., description='任务状态(未开始、进行中)')
    description: str = Field(..., description='任务描述')
    progress: int = Field(..., description='当前完成度')
    priority: int = Field(..., description='优先级')
    is_archived: bool = Field(..., description='是否完成', alias='isArchived')
    created_time: datetime = Field(..., description="创建时间", alias='createdTime')

    class Config:
        from_attributes = True
        validate_by_name = True


class MyFavoriteLinkOut(BaseModel):
    title: str = Field(..., description='收藏文章标题')
    url: str = Field(..., description='收藏文章url')
    favicon_url: str = Field(..., description='收藏文章网站icon url', alias='faviconUrl')
    is_out_of_wall: bool = Field(..., description='是否墙外', alias='isOutOfWall')

    class Config:
        from_attributes = True
        validate_by_name = True
