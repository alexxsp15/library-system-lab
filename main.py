import unittest
from unittest.mock import patch
import io
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import main
from library import Library
from book import Catalog


class TestMainExecution(unittest.TestCase):

    def setUp(self):
        # Повне очищення синглтонів перед запуском головного сценарію
        Library._instance = None
        Catalog._instance = None

    def tearDown(self):
        # Повне очищення після завершення тесту
        Library._instance = None
        Catalog._instance = None

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_scenario_executes_without_errors(self, mock_stdout):
        """Перевірка інтеграційного запуску main.py: сценарій має пройти без винятків (Exceptions)"""
        try:
            main()
        except Exception as e:
            self.fail(f"Головний бізнес-сценарій у main() впав із критичною помилкою: {e}")

        # Зчитуємо перехоплений вивід консолі
        output = mock_stdout.getvalue()

        # Перевіряємо наявність ключових текстових тригерів, які свідчать про успішний прогон сценарію
        self.assertIn("[Подія] Бібліотекар додає книгу: 'Дизайн-патерни в Python'", output)
        self.assertIn("Аліса: Нова книга доступна - Дизайн-патерни в Python", output)
        self.assertIn("Боб: Нова книга доступна - Дизайн-патерни в Python", output)
        self.assertIn("EmailAlert: Надіслано лист про книгу \"Дизайн-патерни в Python\" на admin@library.com", output)


if __name__ == '__main__':
    unittest.main()