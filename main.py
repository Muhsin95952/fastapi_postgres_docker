from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
items = []

# Pydantic model
class Item(BaseModel):
    id: int
    name: str
    position: str 
    phone: int = None



# Create
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item added", "item": item}

# Read all
@app.get("/items")
def read_items():
    return items

# Read one
@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"message": "Item not found"}

# Update
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for i in range(len(items)):
        if items[i].id == item_id:
            items[i] = updated_item
            return {"message": "Item updated", "item": updated_item}
    return {"message": "Item not found"}

# Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i in range(len(items)):
        if items[i].id == item_id:
            deleted = items.pop(i)
            return {"message": "Item deleted", "item": deleted}
    return {"message": "Item not found"}
