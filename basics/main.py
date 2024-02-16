from fastapi import FastAPI, Response, Request, status
from basic_crud import posts, normal_post_list, find_post
from post_model import Post

app = FastAPI()

@app.get("/") # path Operation
def root():
    return {"message": "Welcome to FastAPI !!!"}

@app.get('/getposts/{id}')
def all_posts(id):
    return {
        "data": f"Will show the post of id {id}"
    }

@app.post("/basicpost")
def basicpost(new_post: Post):
    return {
        "message": "Post Created Successfully",
        "post": new_post
    }

# Create a post via Model
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


@app.post('/addpost')
def add_post(request: Request):
    post = request.body
    return {
        "data": post
    }

@app.get('/latest')
def get_latest_post():
    post = normal_post_list[len(normal_post_list)-1]
    return {
        "data": post
    }

# get post from the normal post list
@app.get('/findpost/{id}')
def get_post_by_id(id:int, response: Response):
    post = find_post(int(id))
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        # status = response.status_code = 200
        response.status_code = status.HTTP_200_OK
    return {
        "status": response.status_code,
        "post": post
    }


