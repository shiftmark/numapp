from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data_types import Request, Task, Result
from celery.result import AsyncResult
from celery_worker import sleep_for

app = FastAPI()

@app.get('/')
def read_root():
    return {'All': 'good!'}

@app.post('/item', response_model=Task, status_code=202)
async def request(item: Request):

    task_id = sleep_for.delay(item.item_id)
    res = {'task_id': str(task_id), 'status': 'Processing (post)...'}

    return res

@app.get('/result/{task_id}', response_model=Result, status_code=200)
async def result(task_id):

    task_result = AsyncResult(task_id)
    if not task_result.ready():
        res_not_ready = JSONResponse(
            status_code=202,
            content={'task_id': str(task_id),
                     'status': 'Processing...'}
            )
        return res_not_ready

    res_ready = {'task_id': task_id, 'status': str(task_result.get())}

    return res_ready
