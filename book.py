from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID
from books import books

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    rating: int


BOOKS = []


@app.get('/')
async def get_all_books():
    return books


@app.get('/{author}')
async def get_one_book(author):
    return {"author": author}


@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return book
