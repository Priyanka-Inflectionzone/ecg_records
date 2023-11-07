from pydantic import BaseModel
from typing import List

class ECGHeadersCreateModel(BaseModel):
    RecordName: str
    NumberOfSignals: int
    SignalNames: List[str]
    SamplingFrequency: int
    NumberOfSamples: int
    FileName: str
    SignalUnits: List[str]

class ECGHeadersResponseModel(BaseModel):
    id: str
