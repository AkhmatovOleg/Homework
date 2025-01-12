from fastapi import FastAPI, Path, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def get_user() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[
    str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> User:
    user_id = len(users) + 1
    new_user = User(id=user_id, username=username, age=age)
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

