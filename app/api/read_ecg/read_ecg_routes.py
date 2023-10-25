from fastapi import APIRouter, Depends, status
from fastapi import Request
from fastapi.responses import JSONResponse
from app.api.read_ecg.read_ecg_handler import read_ecg_
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
        data = await read_ecg_(record, db_session)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Record Converted Successfully"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Internal Server Error"})

