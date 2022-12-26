from enum import Enum
from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    "book_1": {"title": "Title One", "author": "Author One"},
    "book_2": {"title": "Title Two", "author": "Author Two"},
    "book_3": {"title": "Title Three", "author": "Author Three"},
    "book_4": {"title": "Title Four", "author": "Author Four"},
    "book_5": {"title": "Title Five", "author": "Author Five"},
}

class BookID(str, Enum):
    book_1 = "book_1"
    book_2 = "book_2"
    book_3 = "book_3"
    book_4 = "book_4"
    book_5 = "book_5"

@app.get("/")
async def get_all_books():
    return BOOKS

@app.get("/skip_book")
async def skip_book(book_id :BookID = None):
    if book_id:
        new_books = BOOKS.copy()
        del new_books[book_id]
        return new_books
    return BOOKS

@app.get("/get_book")
async def get_book(book_id: str):
    return BOOKS[book_id]

# path parameter using enum
# path parameter should be after all the other paths like '/skip_books'
# otherwise when we request '/skip_books' will it will look into '/{book_nr}
@app.get("/{book_id}")
async def get_book(book_id: BookID):
    return BOOKS[book_id]

# add_book need not be before @app.get("/{book_id}") as its a different http method (post)
@app.post("/add_book")
async def add_book(title: str, author: str):
    new_book_id = len(BOOKS)+1
    BOOKS[f"book_{new_book_id}"] = {"title": title, "author": author}
    return BOOKS[f"book_{new_book_id}"]

@app.put("/update/{book_id}")
async def update_book(book_id: str, title: str, author: str):
    BOOKS[book_id] = {"title": title, "author": author}
    return BOOKS[book_id]

@app.delete("/delete/{book_id}")
async def delete_book(book_id: str):
    del BOOKS[book_id]
    return f"Book with id '{book_id}' deleted"

@app.delete("/delete")
async def delete(book_id: str):
    del BOOKS[book_id]
    return f"Book with id '{book_id}' deleted with query param"

