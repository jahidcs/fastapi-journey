from fastapi import FastAPI

app = FastAPI()

@app.get("/") # path Operation
def root():
    return {"message": "Welcome to FastAPI !!!"}