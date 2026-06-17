from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BookSearch(ABC):
    @abstractmethod
    def find_by_criteria(self, criteria: Dict[str, Any]) -> List[Any]:
        pass

    @abstractmethod
    def check_availability(self, book_id: int) -> bool:
        pass


class Notifier(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass