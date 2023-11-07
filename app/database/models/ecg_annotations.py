from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base
from app.common.utils import generate_uuid4

class ECGAnnotation(Base):
    __tablename__ = "ecg_annotations"

    id = Column(String(36), primary_key=True, index=True, default=generate_uuid4)
    RecordName = Column(String(36), index=True)
    Sample = Column(String(256))
    Symbol = Column(String(256))
    Subtype = Column(String(256))
    Chan = Column(String(256))
    Num = Column(String(256))
    AnnotationLength = Column(Integer)