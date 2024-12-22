from typing import List, Dict

from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}
        self.rented_books: Dict[str: Dict[str: int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):

        for username, books in self.rented_books.items():
            if book_name in books.keys():
                return f'The book "{book_name}" is already rented and will be available in' \
                        f' {books[book_name]} days!'

        user.books.append(book_name)
        if user.username not in self.rented_books.keys():
            self.rented_books[user.username] = {}
        self.rented_books[user.username][book_name] = days_to_return

        self.books_available[author].remove(book_name)

        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        self.rented_books[user.username].pop(book_name)








