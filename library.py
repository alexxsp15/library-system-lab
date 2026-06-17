from book import Catalog
from interfaces import Notifier

class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.catalog = Catalog()  # Singleton-каталог книг
            cls._instance._observers = []      # Список об'єктів типу Notifier
        return cls._instance

    # Отримуємо Notifier через метод (Dependency Injection за інтерфейсом)
    def attach(self, observer: Notifier):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Notifier):
        self._observers.remove(observer)

    def notify(self, data: str):
        for observer in self._observers:
            observer.notify(data)  # Виклик методу інтерфейсу

    def add_book_to_library(self, book_title: str):
        print(f"\n[Подія] Бібліотекар додає книгу: '{book_title}'")
        self.catalog.add_book(book_title)
        self.notify(book_title)