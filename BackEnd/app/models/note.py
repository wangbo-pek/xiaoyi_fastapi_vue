"""
    path: xiaoyi/BackEnd/app/models/note.py
    description: 文章笔记note的模型
"""

from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, DateTime, Boolean, Integer
from app.core.database import Base

