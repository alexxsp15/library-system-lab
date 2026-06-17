from interfaces import BookSearch

class User:
    def __init__(self, user_id: int, full_name: str, email: str):
        self.id = user_id
        self.full_name = full_name
        self.email = email

    def get_contact_info(self) -> str:
        return f"{self.full_name} ({self.email})"


class Librarian(User):
    def __init__(self, user_id: int, full_name: str, email: str, access_level: str):
        super().__init__(user_id, full_name, email)
        self.access_level = access_level


class Reader(User):
    def __init__(self, user_id: int, full_name: str, email: str, address: str, phone: str):
        super().__init__(user_id, full_name, email)
        self.address = address
        self.phone = phone

    # Демонстрація використання інтерфейсу: не залежимо від Catalog напряму
    def search_books(self, search_engine: BookSearch, title_query: str):
        return search_engine.find_by_criteria({"title": title_query})