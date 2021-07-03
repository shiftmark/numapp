from fastapi import FastAPI
from fastapi.responses import JSONResponse
from d_types import Request, Task, Result
from celery.result import AsyncResult
from celery_worker import queue_item

app = FastAPI()

@app.get("/")
def read_root():
    return {"All": "good!"}

@app.post("/item", response_model=Task, status_code=202)
async def retr_item(item:Request):
    task_id = queue_item.delay(item.item_id)
    return {"task_id": str(task_id), "status": "Processing"}

@app.get("/result/{task_id}", response_model=Result, status_code=200)
async def get_result(task_id):
    task_result = AsyncResult(task_id)
    if not task_result.ready():
        return JSONResponse(
            status_code=202,
            content={'task_id': str(task_id),
            'status': 'Processing...'}
            )
    result = task_result.get()
    return {'task_id': task_id, 'status': str(result)}
