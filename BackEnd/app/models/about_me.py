"""
    path: xiaoyi/BackEnd/app/models/my_detail.py
    description: 我的个人信息
"""
from datetime import datetime
from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class MyDetail(Base):
    __tablename__ = 'my_detail'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='个人信息id')
    name: Mapped[str] = mapped_column(String(32), default='王博', nullable=False, comment='名字')
    nickname: Mapped[str] = mapped_column(String(32), default='Wang', nullable=False, comment='昵称')
    avatar: Mapped[str] = mapped_column(String(500), nullable=False, comment='我的头像')
    motto: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的座右铭')
    email: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的邮箱')
    wechat: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的微信')
    wechat_qr: Mapped[str] = mapped_column(String(500), nullable=True, comment="微信添加好友二维码")
    city: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的城市')
    short_intro: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的简短介绍')
    full_intro: Mapped[str] = mapped_column(String(300), nullable=False, comment='我的完整介绍')
    wisdom: Mapped[str] = mapped_column(String(500), nullable=False, comment='我的智慧语句')


class MyAbility(Base):
    __tablename__ = 'my_ability'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='我的能力id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的能力维度')
    description: Mapped[str] = mapped_column(String(100), nullable=False, comment='能力描述')
    degree: Mapped[int] = mapped_column(Integer, nullable=False, comment='掌握程度')


class MySkill(Base):
    __tablename__ = 'my_skill'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='我的技能id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的技能维度')
    description: Mapped[str] = mapped_column(String(100), nullable=False, comment='技能描述')
    degree: Mapped[int] = mapped_column(Integer, nullable=False, comment='掌握程度')


class MyTask(Base):
    __tablename__ = 'my_task'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='我的任务id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='我的任务名称')
    status: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='任务状态(未开始、进行中)')
    description: Mapped[str] = mapped_column(String(100), nullable=False, comment='任务描述')
    progress: Mapped[int] = mapped_column(Integer, nullable=False, comment='当前完成度')
    priority:Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment='优先级')
    is_archived: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='是否完成')
    created_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now,
                                                   nullable=False, comment='创建时间')


class MyFavoriteLink(Base):
    __tablename__ = 'my_favorite_link'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment='收藏文章id')
    title: Mapped[str] = mapped_column(String(100), nullable=False, comment='收藏文章标题')
    url: Mapped[str] = mapped_column(String(500), nullable=False, comment='收藏文章url')
    favicon_url: Mapped[str] = mapped_column(String(500), nullable=False, comment='收藏文章网站icon url')
    is_out_of_wall: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='是否墙外')