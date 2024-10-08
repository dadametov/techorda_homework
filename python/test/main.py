from fastapi import FastAPI

app=FastAPI()

@app.get("/hello")
def hello():
    return{"hello":"world"}

@app.post("/create")
def create(item):
    return{"newitem":"item"}