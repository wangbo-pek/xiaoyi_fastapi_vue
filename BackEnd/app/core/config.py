from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # 数据库配置
    DATABASE_URL: str = Field(..., description="MySQL数据库连接符")

    # oss配置
    OSS_ACCESS_KEY_ID:str = Field(..., description="OSS的AccessKey ID")
    OSS_ACCESS_KEY_SECRET:str = Field(..., description="OSS的AccessKey Secret")
    OSS_BUCKET_NAME:str = Field(..., description="OSS的Bucket Name")
    OSS_ENDPOINT:str = Field(..., description="OSS的Endpoint")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()