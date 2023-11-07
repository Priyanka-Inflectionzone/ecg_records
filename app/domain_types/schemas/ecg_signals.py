from pydantic import BaseModel
from typing import List

class ECGSignalDataCreate(BaseModel):
    RecordName: str
    SamplingFrequency: int
    Signals: List[List[float]]

class ECGSignalDataResponse(ECGSignalDataCreate):
    id: str