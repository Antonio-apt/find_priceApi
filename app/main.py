from typing import List, Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from FindPrice import find_price as fp

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/find/{product}")
async def read_item(product: str, limit: Optional[int] = Query(24, gt=0, le=24)):
    """
        Procura o produto no site americanas.com
    """
    return (fp.find_product(product, limit))