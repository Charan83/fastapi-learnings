from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4


app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    rating: int

BOOKS = []



@app.get("/")
async def get_books():
    return BOOKS