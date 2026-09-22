from fastapi import FastAPI
app = FastAPI() 
@app.get("/")
def home():
    return{"page": "home"}
@app.get("/about")
def about():
    return{"page": "about","author": "Rakesh"}

@app.get("/health")
def health():
    return{"status": "ok"}#adding

#Post request
@app.post("/create")
def create_something():
    return {"message":"Created"}
