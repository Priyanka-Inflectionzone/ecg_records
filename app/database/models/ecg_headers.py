from sqlalchemy import Column, Integer, String
from app.database.base import Base
from app.common.utils import generate_uuid4

class ECGHeader(Base):
    __tablename__ = "ecg_headers"

    id = Column(String(36), primary_key=True, index=True, default=generate_uuid4)
    record_name = Column(String(36), unique=True, index=True)
    num_signals = Column(Integer)
    signal_names = Column(String(100))
    sampling_frequency = Column(Integer)
    num_samples = Column(Integer)
    file_name = Column(String(36))
    signal_units = Column(String(100))
