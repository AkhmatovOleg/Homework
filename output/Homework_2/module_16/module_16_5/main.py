from fastapi import FastAPI, Path, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="output/Homework_2/module_16/module_16_5/templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def get_all_user(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get(path="/user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[
    str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> User:
    users_id = len(users) + 1
    new_user = User(id=users_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: int, username: Annotated[
    str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> User:
    try:
        users[user_id - 1] = User(id=user_id, username=username, age=age)
        return users[user_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    for i, t in enumerate(users):
        if t.id == user_id:
            del_user = users.pop(i)
            return del_user
    raise HTTPException(status_code=404, detail="User was not found")
