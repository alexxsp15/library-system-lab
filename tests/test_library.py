# tests/test_library.py
import unittest
from unittest.mock import Mock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from library import Library
from interfaces import Notifier


class TestLibrarySingletonAndObserver(unittest.TestCase):

    def setUp(self):
        Library._instance = None
        self.library = Library()

    def tearDown(self):
        Library._instance = None

    def test_library_singleton_uniqueness(self):
        """Перевірка унікальності екземпляра Library"""
        another_library = Library()
        self.assertIs(self.library, another_library)

    def test_observer_attach_and_notify(self):
        """Перевірка реєстрації спостерігача та надсилання сповіщення"""
        mock_notifier = Mock(spec=Notifier)

        self.library.attach(mock_notifier)
        self.library.notify("Тестова подія")

        mock_notifier.notify.assert_called_once_with("Тестова подія")

    def test_observer_detach(self):
        """Перевірка видалення спостерігача зі списку розсилки"""
        mock_notifier = Mock(spec=Notifier)

        self.library.attach(mock_notifier)
        self.library.detach(mock_notifier)
        self.library.notify("Подія після видалення")

        mock_notifier.notify.assert_not_called()

    def test_add_book_to_library_triggers_notification(self):
        """Інтеграційний тест методу додавання книги, що тригерить нотифікацію моків"""
        mock_notifier1 = Mock(spec=Notifier)
        mock_notifier2 = Mock(spec=Notifier)

        self.library.attach(mock_notifier1)
        self.library.attach(mock_notifier2)

        self.library.add_book_to_library("Дюна")

        mock_notifier1.notify.assert_called_once_with("Дюна")
        mock_notifier2.notify.assert_called_once_with("Дюна")


if __name__ == '__main__':
    unittest.main()