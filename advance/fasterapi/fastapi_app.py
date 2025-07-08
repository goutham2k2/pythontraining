# fastapi_app.py
from fastapi import FastAPI
from django.conf import settings

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()  # Setup Django ORM and models

app = FastAPI()

@app.get("/fastapi/")
def read_root():
    return {"message": "Hello from FastAPI + Django ORM!"}
