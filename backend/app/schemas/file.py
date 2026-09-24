from calendar import day_name
from pydantic import BaseModel
from typing import Optional
from pydantic import Field

class FileResponse(BaseModel):
    original_name: str 
    content_type: str 
    size: int 
    disk_name: str
    url: str
            
        