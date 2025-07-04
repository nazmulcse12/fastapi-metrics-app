from fastapi import APIRouter

router = APIRouter()

@router.get("/data")
def get_data():
    return {"data": "sample"}

@router.post("/data")
def post_data(payload: dict):
    return {"received": payload}
