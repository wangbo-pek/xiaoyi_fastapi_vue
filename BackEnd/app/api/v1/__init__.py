from fastapi import APIRouter
from BackEnd.app.api.v1 import note, diary, test

api_router = APIRouter()
api_router.include_router(note.router, tags=['Note'])
api_router.include_router(diary.router, tags=['Diary'])
api_router.include_router(test.router, tags=['Diary'])