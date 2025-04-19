import boto3
from config import settings

class S3Service:
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION_NAME
        )
        self.bucket_name = settings.AWS_S3_BUCKET_NAME

    def upload_file(self, file, key: str):
        self.s3.upload_fileobj(file, self.bucket_name, key)
        return f"https://{self.bucket_name}.s3.{settings.AWS_REGION_NAME}.amazonaws.com/{key}"

    def delete_file(self, key: str):
        self.s3.delete_object(Bucket=self.bucket_name, Key=key)
        return True