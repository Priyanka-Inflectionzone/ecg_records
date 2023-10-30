from fastapi import APIRouter, Depends, status
from fastapi import Request
from fastapi.responses import JSONResponse
from app.api.ecg.ecg_handler import read_ecg_, write_ecg_
from app.database.db_accessor import get_db_session

###############################################################################

router = APIRouter(
    prefix="/ecg",
    tags=["tests"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

###############################################################################

@router.post("/read-ecg-data")
async def read_ecg(record: Request, db_session = Depends(get_db_session)):
    try:
       record_data = await record.json()
       dataset_dir = record_data.get('dirName')
       record_name = record_data.get('recordName')
       extension = record_data.get('extension')
       data = await read_ecg_(dataset_dir, record_name, extension, db_session)
       return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Record Converted Successfully"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Internal Server Error"})

@router.post("/write-ecg-data")
async def read_ecg(record: Request):
    try:
       data = await write_ecg_(record)
       return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Record Converted Successfully"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Internal Server Error"})