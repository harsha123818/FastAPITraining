from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return{"message":"Hello world","numer":44,"is fun":True}
