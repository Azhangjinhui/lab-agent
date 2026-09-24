
import os
import shutil
import time
from urllib import response
import uuid

from app.common.exceptions import BusinessException
from app.common.response import Response
from app.config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE, UPLOAD_DIR
from fastapi import APIRouter, File, UploadFile
from pathlib import Path

from app.schemas.file import FileResponse

router = APIRouter(prefix='/file', tags=['文件上传'])
@router.post('/upload')
async def upload_file(file: UploadFile = File(...)):  # noqa: B008
    if not file.filename:
       raise BusinessException(message="文件名不能为空")
    filename = os.path.basename(file.filename)
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise BusinessException(message="文件格式错误")
    if file.size and file.size > MAX_FILE_SIZE:
        raise BusinessException(message=f"文件大小不能超过{MAX_FILE_SIZE}字节")
    disk_name = f"{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}{ext}"
    save_path = UPLOAD_DIR / disk_name
    with open(save_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    return Response.success(
        data=FileResponse(
            original_name=filename,
            content_type=file.content_type,
            size=file.size,
            disk_name=disk_name,
            url=f"/upload/{disk_name}",
        )
    )

    
    
 

   



