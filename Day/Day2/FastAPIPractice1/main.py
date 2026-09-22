from fastapi import FastAPI
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