from pydantic import BaseModel
from typing import List

class ECGAnnotationCreate(BaseModel):
    record_name: str
    time: float
    sample: int
    annotation: str
    sub: str
    chan: str
    num: str

class ECGAnnotationResponse(ECGAnnotationCreate):
    id: str