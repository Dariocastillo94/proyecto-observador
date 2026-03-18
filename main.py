from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Sistemas operativos en linea","version": "1.0.0"}

@app.get("/health")
def healthCheck():
    return {"status": "healthy", "container_id": os.uname()[1]}