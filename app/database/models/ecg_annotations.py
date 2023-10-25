from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base
from app.common.utils import generate_uuid4

class ECGAnnotation(Base):
    __tablename__ = "ecg_annotations"

    id = Column(String(36), primary_key=True, index=True, default=generate_uuid4)
    record_name = Column(String(36), index=True)
    time = Column(Float)
    sample = Column(Integer)
    annotation = Column(String(36))
    sub = Column(String(36))
    chan = Column(String(36))
    num = Column(String(36))