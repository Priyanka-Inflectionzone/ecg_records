from sqlalchemy import Column, Integer, String
from app.database.base import Base
from app.common.utils import generate_uuid4

class ECGHeader(Base):
    __tablename__ = "ecg_headers"

    id = Column(String(36), primary_key=True, index=True, default=generate_uuid4)
    RecordName = Column(String(36), unique=True, index=True)
    NumberOfSignals = Column(Integer)
    SignalNames = Column(String(100))
    SamplingFrequency = Column(Integer)
    NumberOfSamples = Column(Integer)
    FileName = Column(String(36))
    SignalUnits = Column(String(100))
