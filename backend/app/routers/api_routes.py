from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from fastapi.responses import JSONResponse
import os
import shutil
import uuid
from app.middlewares.auth import get_current_user
from app.schemas.schema import UserResponse
from app.models.user import User

router = APIRouter(
    prefix="/api",
)

upload_dirs = {
    "files": "./uploads/files",
}

for path in upload_dirs.values():
    os.makedirs(path, exist_ok=True)

@router.post("/user-input")
async def user_input(
    prompt: str = Form(None),
    file: UploadFile = File(None)
):
    if not prompt and not file:
        raise HTTPException(status_code=400, detail="No input provided")

    response = {}
    
    if file:
        file_path = os.path.join(upload_dirs["files"], file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        response["file_saved"] = file.filename

    return JSONResponse(content={
        "message": "Input successfully received",
    })



@router.get('/me', summary='Get details of currently logged in user', response_model=UserResponse)
async def get_me(user: User = Depends(get_current_user)):
    return user