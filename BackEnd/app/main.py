from fastapi import FastAPI
from app.api.v1 import api_router

app = FastAPI(
    title="XiaoYi_Blog",
    description="博客",
    version="1.0",
    contact={
        "name":"wang",
        "url":"https://wang.com",
        "email":"wangbo.pek@gmail.com"
    },
    docs_url="/docs",
    redoc_url="/redoc"
)
app.include_router(api_router, prefix="/api/v1")
