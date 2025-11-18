from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    length: int
    quantity: int

@app.post("/")
async def process_items(items: List[Item]):
    # items will be a list of Item objects
    total_quantity = sum(item.quantity for item in items)
    total_length = sum(item.length * item.quantity for item in items)

    return {
        "received_count": len(items),
        "total_quantity": total_quantity,
        "total_length": total_length,
        "items": items
    }