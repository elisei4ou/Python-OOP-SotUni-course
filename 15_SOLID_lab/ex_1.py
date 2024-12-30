from typing import List


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
            return f'Book "{book.title}" with {book.author} author successfully added'
        return "Book already added"

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            return f'Book "{book.title}" with {book.author} author successfully removed'
        return "Book doesn't exist"

    def find_book(self, title: str):
        try:
            return next(filter(lambda x: x.title == title, self.books))
        except StopIteration:
            return f"No such book with {title} title!"