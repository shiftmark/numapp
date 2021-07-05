from pydantic import BaseModel

class Request(BaseModel):
    item_id: str

class Task(BaseModel):
    task_id: str
    status: str

class Result(BaseModel):
    task_id: str
    status: str
    