import unittest
import sys
import os

# Налаштування шляху для імпорту модулів із кореня проекту
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from book import Book, Catalog


class TestBookAndCatalog(unittest.TestCase):

    def setUp(self):
        # Ініціалізація фікстур для кожного тесту
        self.book = Book(book_id=99, title="Тестова Книга", author="Тестовий Автор", copies=2)
        # Очищуємо стан синглтону каталогу перед кожним тестом
        Catalog._instance = None
        self.catalog = Catalog()

    def tearDown(self):
        # Скидаємо стан синглтону після кожного тесту для ізоляції середовища
        Catalog._instance = None

    # --- ТЕСТУВАННЯ ВИНЯТКОВИХ СИТУАЦІЙ (Вимога п.6.2) ---

    def test_book_negative_copies_raises_error(self):
        """Перевірка, що створення книги з від'ємною кількістю копій викликає ValueError"""
        with self.assertRaises(ValueError):
            Book(book_id=100, title="Некоректна Книга", author="Автоматика", copies=-5)

    # --- ТЕСТУВАННЯ СТАНУ ТА ЛОГІКИ ОБ'ЄКТІВ ---

    def test_book_initial_state(self):
        """Перевірка ініціалізації початкового стану книги"""
        self.assertEqual(self.book.id, 99)
        self.assertEqual(self.book.title, "Тестова Книга")
        self.assertEqual(self.book.author, "Тестовий Автор")
        self.assertEqual(self.book.copies, 2)

    def test_book_is_available_true(self):
        """Книга доступна, якщо кількість копій > 0"""
        self.assertTrue(self.book.is_available())

    def test_book_is_available_false(self):
        """Книга недоступна, якщо кількість копій == 0"""
        self.book.copies = 0
        self.assertFalse(self.book.is_available())

    # --- ТЕСТУВАННЯ СИНГЛТОНУ ТА КОЛЕКЦІЙ ---

    def test_catalog_singleton_uniqueness(self):
        """Перевірка, що Catalog є унікальним екземпляром (Singleton)"""
        another_catalog = Catalog()
        self.assertIs(self.catalog, another_catalog)

    def test_catalog_add_book_and_total(self):
        """Перевірка додавання книги та підрахунку загальної кількості"""
        self.assertEqual(self.catalog.get_total_books(), 0)
        self.catalog.add_book("Python Advanced")
        self.assertEqual(self.catalog.get_total_books(), 1)

    def test_catalog_find_by_criteria_title(self):
        """Пошук книги за назвою через інтерфейс BookSearch"""
        self.catalog.add_book("Clean Code")
        results = self.catalog.find_by_criteria({"title": "Clean Code"})
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Clean Code")

    def test_catalog_check_availability_success(self):
        """Перевірка доступності книги за її ID в каталозі"""
        self.catalog.add_book("Refactoring")
        # Новій книзі присвоюється ID = 1 (згідно з логікою Catalog.add_book)
        self.assertTrue(self.catalog.check_availability(1))

    def test_catalog_check_availability_not_found(self):
        """Перевірка доступності для неіснуючого ID книги"""
        self.assertFalse(self.catalog.check_availability(999))


if __name__ == '__main__':
    unittest.main()