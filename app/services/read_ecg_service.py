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

class ReadEcgService:
    async def read_header(db: Session, dataset_dir, record_name) -> ECGHeadersResponseModel:

        record_headers = wfdb.rdheader(record_name, pb_dir=dataset_dir)

        db_record = ECGHeader(
        RecordName=record_headers.record_name,
        NumberOfSignals=record_headers.n_sig,
        SignalNames=record_headers.sig_name,
        SamplingFrequency=record_headers.fs,
        NumberOfSamples=record_headers.sig_len,
        FileName=record_headers.file_name,
        SignalUnits=record_headers.units,
        )

        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record.__dict__

    async def read_signals(db: Session, dataset_dir, record_name) -> ECGSignalDataResponse:

        signal_data, fields = wfdb.rdsamp(record_name, pb_dir=dataset_dir, sampto=1500)

        db_signal_data = ECGSignalData(
           RecordName=record_name,
           SamplingFrequency=fields["fs"],
           Signals=signal_data
        )

        db.add(db_signal_data)
        db.commit()
        db.refresh(db_signal_data)
        return db_signal_data.__dict__

    async def read_annotation(db: Session, dataset_dir, record_name, extension) -> ECGAnnotationResponse:
        try:
            sampling_frequency = 100

            annotations = wfdb.rdann(record_name, extension=extension,  pb_dir=dataset_dir, sampto=1500)

            new_data = {
                'sample' : annotations.sample.tolist(),
                'symbol' : annotations.symbol,
                'subtype': annotations.subtype.tolist(),
                'chan' : annotations.chan.tolist(),
                'num': annotations.num.tolist(),
                'ann_len': annotations.ann_len
            }

            db_annotation = ECGAnnotation(
                RecordName = record_name,
                Sample = new_data['sample'],
                Symbol = new_data['symbol'],
                Subtype = new_data['subtype'],
                Chan = new_data['chan'],
                Num = new_data['num'],
                AnnotationLength = new_data['ann_len']
            )

            db.add(db_annotation)
            db.commit()
            db.refresh(db_annotation)
            return db_annotation.__dict__

        except Exception as e:
            raise e




