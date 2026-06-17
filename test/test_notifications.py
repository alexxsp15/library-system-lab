# tests/test_notifications.py
import unittest
from unittest.mock import patch
import io
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from notifications import UserNotifier, EmailAlert


class TestNotificationsOutput(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_notifier_print(self, mock_stdout):
        """Перевірка виводу в консоль для UserNotifier"""
        notifier = UserNotifier(user_name="Аліса")
        notifier.notify("Кобзар")

        expected_output = "Аліса: Нова книга доступна - Кобзар\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_email_alert_print(self, mock_stdout):
        """Перевірка виводу в консоль для EmailAlert"""
        alert = EmailAlert(email="test@lib.com")
        alert.notify("Кобзар")

        expected_output = 'EmailAlert: Надіслано лист про книгу "Кобзар" на test@lib.com\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()