from fastapi import APIRouter

router = APIRouter()

@router.get("/diaries/")
async def diary_list():
    return None


@router.get("/diaries/{diary_id}/")
async def diary_detail():
    return None



