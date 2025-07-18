from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
import os
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor


app = FastAPI()

# In-memory storage
items = []

# Pydantic model
class Item(BaseModel):
    id: int
    title: str
    content: str 
    likes: int = None
    

try:
    conn = psycopg2.connect(
    host=os.getenv("DATABASE_HOST", "localhost"),
    database=os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    cursor_factory=RealDictCursor
)
    cursor = conn.cursor()
    print("Database connection has been Successfull")
except Exception as error:
    print("Connection cannot Established")
    print("Error: ", error)


# Create
@app.post("/items")
def create_item(item: Item):
    cursor.execute("""
        INSERT INTO posts_db (title, content, likes)
        VALUES (%s, %s, %s)
        RETURNING *;
    """, (item.title, item.content, item.likes))
    new_post = cursor.fetchone()
    conn.commit()
    return {"post": new_post}

# Read all
@app.get("/items")
def read_items():
    cursor.execute(""" select * from posts_db; """)
    post = cursor.fetchall()
    return post

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
