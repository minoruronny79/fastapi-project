from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

students={
    1:
    "name":"john",
    "age":17,
    "year":12
}

@app.get("/")
def index():
    return {"name":"First Data"}