from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[float] = None

post1 = Post(
    title="Hello, Jahid",
    content="Welcome to FastAPI"
)
post2 = Post(
    title="Fast API is Fun",
    content="I like FastAPI a lot",
    rating=4.2
)
post3 = Post(
    title="Fast API is for easy API development",
    content="Fast API is a framework that always focuses of Develop API in a easy and simple way",
    rating=4.9,
    published=True
)

posts = [post1, post2, post3]

normal_post_list = [
    {
        "id": 1,
        "title": "Hello, Jahid",
        "content": "Welcome to FastAPI",
        "published": False,
        "rating": None
    },
    {
        "id": 2,
        "title": "Fast API is Fun",
        "content": "I like FastAPI a lot",
        "published": False,
        "rating": 4.2
    },
    {
        "id": 3,
        "title": "Fast API is for easy API development",
        "content": "Fast API is a framework that always focuses of Develop API in a easy and simple way",
        "published": False,
        "rating": 4.9
    },
    {
        "id": 4,
        "title": "Post API Test",
        "content": "Welcome to FastAPI, Creating a post and append it in list",
        "published": False,
        "rating": 3.2
    }
]

def find_post(id):
    print(normal_post_list)
    for post in normal_post_list:
        if post["id"] == id:
            return post
        
    

@app.get("/") # path Operation
def root():
    return {"message": "Welcome to FastAPI !!!"}

@app.post("/basicpost")
def basicpost(new_post: Post):
    return {
        "message": "Post Created Successfully",
        "post": new_post
        # "post" : {
        #     'title': new_post.title,
        #     'content': new_post.content,
        #     'published': new_post.published,
        #     'rating': new_post.rating
        # }
    }

@app.post('/createpost')
def addpost(new_post: Post):
    post = dict(new_post)
    posts.append(post)
    return {
        "message": "Post added in to list",
        "data": new_post
    }

@app.get('/getposts')
def all_posts():
    return {
        "data": posts
    }

@app.get('/getposts/{id}')
def all_posts(id):
    return {
        "data": f"Will show the post of id {id}"
    }

@app.get('/findpost/{id}')
def get_post_by_id(id):
    post = find_post(int(id))
    return {
        "post": post
    }
