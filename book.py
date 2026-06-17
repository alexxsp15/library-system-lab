from typing import List, Dict, Any
from interfaces import BookSearch

# Оновлений шматочок у book.py
class Book:
    def __init__(self, book_id: int, title: str, author: str, copies: int):
        if copies < 0:
            raise ValueError("Кількість копій не може бути від'ємною!")
        self.id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def is_available(self) -> bool:
        return self.copies > 0


class Catalog(BookSearch):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Catalog, cls).__new__(cls)
            cls._instance.books = []
        return cls._instance

    def add_book(self, book_title: str):
        # Для симуляції створюємо об'єкт Book всередині каталогу
        new_id = len(self.books) + 1
        book = Book(book_id=new_id, title=book_title, author="Unknown", copies=1)
        self.books.append(book)

    def get_total_books(self) -> int:
        return len(self.books)

    # Реалізація інтерфейсу BookSearch
    def find_by_criteria(self, criteria: Dict[str, Any]) -> List[Book]:
        results = []
        for book in self.books:
            if criteria.get("title") == book.title or criteria.get("author") == book.author:
                results.append(book)
        return results

    def check_availability(self, book_id: int) -> bool:
        for book in self.books:
            if book.id == book_id:
                return book.is_available()
        return False