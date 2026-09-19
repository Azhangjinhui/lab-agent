from typing import Any
from pydantic import BaseModel, ConfigDict



class Response(BaseModel):
    code:int
    message:str
    data:Any=None
    model_config=ConfigDict(from_attributes=True)
    @classmethod
    def success(cls,data:Any=None,message:str='请求成功'):
        response=cls(code=200,message=message,data=data)
        return response
    @classmethod
    def error(cls,message:str,code:int=400,data:Any=None):
        response=cls(code=code,message=message,data=data)
        return response
   
