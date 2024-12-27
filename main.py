from fastapi import FastAPI
from database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Geography API!"}
