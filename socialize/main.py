from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None



@app.get("/")
async def root():
    data = {
        "message": "Always contains the same exitement",
    }
    return data


@app.get("/posts")
def post():
    return {"message": "this is your post"}


@app.post("/create")
def create_post(payload: dict = Body(...)):
    return {'data': payload}


@app.post("/createpost")
def create_new_post(new_post: Post):
    payload = {
        'title': new_post.title,
        'content': new_post.content,
        'published': new_post.published,
        'rating': new_post.rating
    }
    return payload