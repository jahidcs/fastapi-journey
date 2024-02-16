from post_model import Post


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
        