from fastapi import APIRouter
from BackEnd.app.api.v1 import note, diary, test, about_me, comment, site_config, tag_category, user, visitor

api_router = APIRouter()
api_router.include_router(note.router)
api_router.include_router(diary.router )
api_router.include_router(test.router)
api_router.include_router(about_me.router )
api_router.include_router(site_config.router)
api_router.include_router(tag_category.router )
api_router.include_router(user.router)
api_router.include_router(visitor.router)
api_router.include_router(comment.router)