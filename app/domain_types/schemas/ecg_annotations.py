from pydantic import BaseModel
from typing import List

class ECGAnnotationCreate(BaseModel):
    RecordName: str
    Sample: List[int]
    Symbol: List[str]
    Subtype: List[int]
    Chan: List[int]
    Num: List[int]
    AnnotationLength: int

class ECGAnnotationResponse(ECGAnnotationCreate):
    id: str