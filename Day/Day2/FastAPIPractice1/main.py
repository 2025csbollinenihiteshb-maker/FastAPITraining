from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def home():
    return {"page":"Home"}
@app.get("/about")
def about():
    return{"page":"About","author":"Charan"}
@app.get("/health")
def health():
    return {"Status":"ok"}
#post request
@app.post("/create")
def create_something():
    return {"message":"Created"}
#path parameters 
@app.get("/student/{usn}")
def get_result(usn):
    return {"Result":"Distinction","usn":usn}



@app.get("/candidate/{roll}")
def get_result(roll: str):
    return {"Result":"Distinction","roll":roll,"type": str(type(roll))}
#pydantic model
class item(BaseModel):
    name: str
    price:float
    in_stock: bool = True
@app.post("/items")
def create_item(item: item):
    return {"recevied":item, "total_price": item.price * 1.18}