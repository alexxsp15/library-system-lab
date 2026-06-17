import unittest
from unittest.mock import Mock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from user import User, Librarian, Reader
from interfaces import BookSearch


class TestUserAndRoles(unittest.TestCase):

    def setUp(self):
        # ВИНЕСЕННЯ СПІЛЬНИХ НАЛАШТУВАНЬ (Вимога п.6.1)
        # Створюємо мок-заглушку для інтерфейсу пошуку книг один раз для всіх тестів
        self.mock_search_engine = Mock(spec=BookSearch)

        # Заздалегідь підготовлені тестові сутності (Fixtures)
        self.shared_user = User(user_id=1, full_name="Іван Іванов", email="ivan@example.com")
        self.shared_reader = Reader(user_id=3, full_name="Олексій", email="alex@test.com", address="Київ",
                                    phone="12345")

    def test_user_get_contact_info(self):
        """Перевірка форматування контактної інформації користувача за допомогою фікстури setUp"""
        self.assertEqual(self.shared_user.get_contact_info(), "Іван Іванов (ivan@example.com)")

    def test_librarian_access_level(self):
        """Перевірка специфічного атрибута класу Librarian"""
        librarian = Librarian(user_id=2, full_name="Марія Петрівна", email="maria@lib.com", access_level="Admin")
        self.assertEqual(librarian.access_level, "Admin")
        self.assertEqual(librarian.full_name, "Марія Петрівна")

    def test_reader_search_books_via_mock(self):
        """Перевірка пошуку книг за допомогою спільного Mock-об'єкта для інтерфейсу BookSearch"""
        # Налаштовуємо індивідуальну поведінку моку для цього тесту
        self.mock_search_engine.find_by_criteria.return_value = ["Знайдена книга"]

        # Використовуємо створений у setUp об'єкт читача
        results = self.shared_reader.search_books(self.mock_search_engine, "Паттерни")

        # Перевірки (Assertions)
        self.assertEqual(results, ["Знайдена книга"])
        # Перевіряємо, чи метод моку викликався саме з тими параметрами, які очікував Reader
        self.mock_search_engine.find_by_criteria.assert_called_once_with({"title": "Паттерни"})


if __name__ == '__main__':
    unittest.main()