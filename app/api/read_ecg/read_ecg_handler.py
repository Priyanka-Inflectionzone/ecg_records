from app.services.read_ecg_service import ReadEcgService
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


