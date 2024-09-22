from typing import Union
import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    a = ['1', '2', '3', '4', '5']
    return random.choice(a)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}