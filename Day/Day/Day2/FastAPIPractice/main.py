from fastapi import FastAPI
from pydantic import BaseModel
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

#Path parameter with type hint
@app.get("/student/{usn}")
def get_result(usn):
    return {"Result":"Distinction","usn":usn}

@app.get("/candidate/{rollno}")
def get_candidate(rollno):
    return {"Result":"Distinction","rollno":rollno,"type":str(type(rollno))}

#pydantic package
class item(BaseModel):
    name:str
    price:float
    in_stock:bool = True

@app.post("/items")
def create_item(item:item):
    return{"received":item, "total_price":item.price*1.18}




