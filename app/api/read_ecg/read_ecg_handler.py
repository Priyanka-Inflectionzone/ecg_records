from app.services.read_ecg_service import EcgService

async def read_ecg_(record, db_session):
    try:
       headers = await EcgService.read_header(db_session, record)
       data = await EcgService.read_signals( db_session, record)
       annotations = await EcgService.read_annotations( db_session, record)
       message = "Records created successfully"
       return {headers, data, annotations}
    except Exception as e:
        raise e
    finally:
        db_session.close()


