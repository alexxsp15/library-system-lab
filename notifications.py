from interfaces import Notifier

class UserNotifier(Notifier):
    def __init__(self, user_name: str):
        self.user_name = user_name

    def notify(self, message: str) -> None:
        print(f"{self.user_name}: Нова книга доступна - {message}")


class EmailAlert(Notifier):
    def __init__(self, email: str):
        self.email = email

    def notify(self, message: str) -> None:
        print(f"EmailAlert: Надіслано лист про книгу \"{message}\" на {self.email}")