from app.services.read_ecg_service import EcgService
from fastapi import Request

async def read_ecg_(dataset_dir, record_name, extension, db_session):
    try:
       headers = await EcgService.read_header(db_session, dataset_dir, record_name)
       data = await EcgService.read_signals( db_session, dataset_dir, record_name)
       annotations = await EcgService.read_annotation(db_session, dataset_dir, record_name, extension)
       message = "Records created successfully"
       return {headers, data, annotations}
    except Exception as e:
        raise e
    finally:
        db_session.close()


