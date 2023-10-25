from sqlalchemy import Column, Integer, String
from app.database.base import Base
from app.common.utils import generate_uuid4

class ECGSignalData(Base):
    __tablename__ = "ecg_signal_data"

    id = id = Column(String(36), primary_key=True, index=True, default=generate_uuid4)
    record_name = Column(String(36), index=True)
    sampling_frequency = Column(Integer)
    signals = Column(String(256))  # Store the signals as a JSON string