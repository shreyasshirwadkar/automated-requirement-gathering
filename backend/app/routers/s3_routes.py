# from fastapi import APIRouter, upload_file, HTTPException, Depends
# from fastapi.responses import JSONResponse
# from bucket.s3_service import S3Service
# import logging

# router = APIRouter(
#     prefix="/s3",
#     tags=["Amazon S3 Operations"],
#     responses={404: {"description": "Not found"}},
# )

# s3_service = S3Service()
# @router.post("/upload")
# async def upload_file(file: upload_file, key: str):
#     try:
#         if not file:
#             raise HTTPException(status_code=400, detail="No file uploaded")