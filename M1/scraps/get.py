from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Mathir": "Hello World"}


fake_names = [
    "Mathir",
    "Alagi",
    "Papa",
    "Mami",
    "Baba",
    "Dada",
    "Chatgpt",
    "Copilot",
    "Davinci",
    "Textcurie",
]


@app.get("/names/")
async def list_names(limit: int = 5):
    return {"names": fake_names[:limit]}


@app.get("/names/{name}")
async def add_name(name: str, add: bool = False):
    if add and name not in fake_names:
        fake_names.append(name)
    return {"name": name}


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
    chatgpt = "chatgpt"
    copilot = "copilot"
    davinci = "davinci"
    textcurie = "textcurie"


@app.get("/model/{model}")
async def read_model(model: Model):
    return {"model_id": model.value, "message": f"Hello {model.value}!"}


@app.get("/names/{name}/age/{age}")
async def read_name(name: str, age: int):
    return {"name": name, "age": age}


class Blog(BaseModel):
    title: str
    content: str
    author: str | None


@app.post("/blog/")
async def create_blog(blog: Blog):
    return {
        "title": blog.title,
        "content": blog.content,
        "author": blog.author or "Anonymous",
    }
