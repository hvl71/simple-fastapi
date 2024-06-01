from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/name/{name}")
def read_name(name: str):
    return {"message": f"Your name is {name}"}
