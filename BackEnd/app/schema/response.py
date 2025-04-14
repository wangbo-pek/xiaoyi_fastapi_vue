"""
    path: xiaoyi/BackEnd/schema/response.py
    description: 所有响应数据最外层的code、message、data的Pydantic模型
"""

from typing import Generic, TypeVar, Optional
from pydantic import Field, BaseModel
from pydantic import ConfigDict


T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    code:int = Field(..., description='自定义响应状态')
    message:str = Field(..., description='自定义提示信息')
    data: Optional[T] = Field(None, description='返回数据内容')

    model_config = ConfigDict(arbitrary_types_allowed=True)