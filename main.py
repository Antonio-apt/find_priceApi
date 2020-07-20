from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from FindPrice import find_price as fp

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/find/{product}")
async def read_item(product: str):
    return fp.find_product(product)