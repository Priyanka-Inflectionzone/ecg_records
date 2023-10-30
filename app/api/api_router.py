from fastapi import APIRouter
from .ecg.ecg_routes import router as record_router
import os

API_PREFIX = os.environ.get("API_PREFIX", "/api/v1")

router = APIRouter(prefix=API_PREFIX)

def add_routes():
    router.include_router(record_router)

add_routes()
