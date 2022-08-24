from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID
from books import books

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=2)
    author: Optional[str]
    description: str = Field(title="description about the book",
                             min_length=5,
                             max_length=100)
    rating: int = Field(gt=-1, lt=101)


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
    return BOOKS
