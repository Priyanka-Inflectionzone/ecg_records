from app.services.read_ecg_service import ReadEcgService
from app.services.write_ecg_service import WriteEcgService
from fastapi import Request

async def read_ecg_(dataset_dir, record_name, extension, db_session):
    try:
       headers = await ReadEcgService.read_header(db_session, dataset_dir, record_name)
       data = await ReadEcgService.read_signals( db_session, dataset_dir, record_name)
       annotations = await ReadEcgService.read_annotation(db_session, dataset_dir, record_name, extension)
       message = "Records created successfully"
       return {headers, data, annotations}
    except Exception as e:
        raise e
    finally:
        db_session.close()


async def write_ecg_(record: Request):
    try:
       record_data = await record.json()
       record_name = record_data.get('recordName')
       sampling_frequency = record_data.get('samplingFrequency')
       number_of_samples = record_data.get('samples')
       signals_data = record_data.get('data')
       data = {
           "record_name": record_name,
           "sampling_frequency": sampling_frequency,
           "number_of_samples": number_of_samples,
           "signals_data": signals_data
           }

       records = await WriteEcgService.create_ecg_records(data)

    except Exception as e:
        raise e