import wfdb
import os
import json
from sqlalchemy.orm import Session
from app.domain_types.schemas.ecg_headers import ECGHeadersResponseModel
from app.domain_types.schemas.ecg_signals import ECGSignalDataResponse
from app.domain_types.schemas.ecg_annotations import ECGAnnotationResponse
from app.database.models.ecg_headers import ECGHeader
from app.database.models.ecg_signals import ECGSignalData
from app.database.models.ecg_annotations import ECGAnnotation

class EcgService:
    def read_header(db: Session, record) -> ECGHeadersResponseModel:
        dataset_dir = record.dirName
        record_name = record.recordName

        record_headers = wfdb.rdheader(record_name, pb_dir=dataset_dir)

        db_record = ECGHeader(
        record_name=record_headers.record_name,
        num_signals=record_headers.n_sig,
        signal_names=record_headers.sig_name,
        sampling_frequency=record_headers.fs,
        num_samples=record_headers.sig_len,
        file_name=record_headers.file_name,
        signal_units=record_headers.units,
        )

        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record.id

    def read_signals(db: Session, record) -> ECGSignalDataResponse:
        dataset_dir = record.dirName
        record_name = record.recordName

        signal_data, _ = wfdb.rdsamp(record_name, pb_dir=dataset_dir, sampto=1500)
        db_signal_data = ECGSignalData(
           record_name=record_name,
           sampling_frequency=_["fs"],
           signals=signal_data.toList()
        )
        db.add(db_signal_data)
        db.commit()
        db.refresh(db_signal_data)
        return db_signal_data.id

    def read_annotation(self, db: Session, record) -> ECGAnnotationResponse:
        dataset_dir = record.dirName
        record_name = record.recordName
        ext = record.extension
        sampling_frequency = 100

        annotations = wfdb.rdann(record_name, extension=ext,  pb_dir=dataset_dir)

        for index in range(len(annotations.sample)):
            time_in_seconds = annotations.sample[index] / sampling_frequency

            db_annotation = ECGAnnotation(
                record_name=annotations.record_name,  # Replace with the appropriate field
                time_ms=time_in_seconds * 1000,  # Convert to milliseconds
                sample=annotations.sample[index],
                annotation=annotations.symbol[index],
                sub=annotations.subtype[index],
                chan=annotations.chan[index],
                num=annotations.num[index]
            )

        db.add(db_annotation)
        db.commit()
        db.refresh(db_annotation)
        return db_annotation.id



