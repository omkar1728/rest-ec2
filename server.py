from fastapi import FastAPI, UploadFile, File
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import boto3
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
ACCESS_SECRET_KEY = os.getenv("ACCESS_SECRET_KEY")
BUCKET_NAME= os.getenv('BUCKET_NAME')

app = FastAPI()
s3 = boto3.client('s3',
                    aws_access_key_id = ACCESS_KEY_ID,
                    aws_secret_access_key = ACCESS_SECRET_KEY,
                )


# # Set up CORS
# origins = [
#     "http://localhost:3000",
    
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
def read_root():
    return "Hello, the fastapi server is running"

@app.get("/getallfiles")
async def hello():
    
    res = s3.list_objects_v2(Bucket=BUCKET_NAME)
    res = res["Contents"]
    print(type(res))
    return res

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if file:
        s3.upload_fileobj(file.file, BUCKET_NAME, file.filename)
        return "file uploaded"
    else:
        return "error in uploading."