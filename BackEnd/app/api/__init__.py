"""
    path: xiaoyi/BackEnd/app/api/__init__.py
    description:
"""

from fastapi import APIRouter
from app.api import note, site_config, user, about_me, tag_category, visitor, comment, diary

api_router = APIRouter()
api_router.include_router(note.router)
api_router.include_router(diary.router)
api_router.include_router(about_me.router)
api_router.include_router(site_config.router)
api_router.include_router(tag_category.router)
api_router.include_router(user.router)
api_router.include_router(visitor.router)
api_router.include_router(comment.router)
