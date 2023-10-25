from pydantic import BaseModel
from typing import List

class ECGSignalDataCreate(BaseModel):
    record_name: str
    sampling_frequency: int
    signals: List[List[float]]

class ECGSignalDataResponse(ECGSignalDataCreate):
    id: str