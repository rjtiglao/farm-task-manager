from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import ToDo

#app object
app = FastAPI()

origins = ['https://localhost:3000']

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo

)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")

def read_root():
    return {"Ping":"Pong"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo{title}", response_model=ToDo)
async def get_todo_by_id(id):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no TODO item with this title")


@app.post("/api/todo", response_model=ToDo)
async def post_todo(todo:ToDo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400,f"Something went wrong / Bad Request")

@app.put("/api/todo{title}")
async def put_todo(title:str, data:str):
    response = await update_todo(title,desc)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO item with this title")     


@app.delete("/api/todo{title}")
async def delete_todo(todo):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo item!"
    raise HTTPException(404, f"there is no TODO item with this title")
    