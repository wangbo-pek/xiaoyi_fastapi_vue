from fastapi import FastAPI
from app.api import api_router
from starlette.middleware.cors import CORSMiddleware
from app.core.config import get_settings

app = FastAPI(
    title="Deep Think",
    description="深邃思考",
    version="1.0.0",
    contact={
        "name": "wang",
        "url": "https://wang.com",
        "email": "wangbo.pek@gmail.com"
    },
    docs_url="/docs",
    redoc_url="/redoc"
)

settings = get_settings()
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
