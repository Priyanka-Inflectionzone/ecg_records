from pydantic import BaseModel
from typing import List

class ECGHeadersCreateModel(BaseModel):
    record_name: str
    num_signals: int
    signal_names: List[str]
    sampling_frequency: int
    num_samples: int
    file_name: str
    signal_units: List[str]

class ECGHeadersResponseModel(BaseModel):
    id: str