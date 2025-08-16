from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Mathir": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/user/admin")
async def read_user():
    return {"user_id": "Mathir"}


@app.get("/user/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


class Model(str, Enum):
    mathir = "mathir"
    alagi = "alagi"
    papa = "papa"


@app.get("/model/{model}")
async def read_model(model: Model):
    return {"model_id": model.value, "message": f"Hello {model.value}!"}


fake_items = [{"name": "Mathir"}, {"name": "Alagi"}, {"name": "Papa"}]


@app.get("/items/")
async def read_items(limit: int = 1):
    return {"items": fake_items[:limit]}
