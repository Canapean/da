class Book:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__genre = genre
        self.__status = True  # True означает "в наличии"

        self.__validate_data()

    def __validate_data(self):
        if not self.__title:
            raise ValueError("Название книги не может быть пустым.")
        if self.__year > 2023:  # Допустим, текущий год - 2023
            raise ValueError("Год издания не может быть в будущем.")

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @property
    def genre(self):
        return self.__genre

    @property
    def status(self):
        return self.__status

    def issue(self):
        if self.__status:
            self.__status = False
            return True
        return False

    def return_book(self):
        self.__status = True


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, file_format: str):
        super().__init__(title, author, year, genre)
        self.__file_format = file_format

    @property
    def file_format(self):
        return self.__file_format


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book: Book):
        self.__books.append(book)

    def find_book(self, title: str) -> Book:
        for book in self.__books:
            if book.title == title:
                return book
        return None

    def remove_book(self, title: str):
        book = self.find_book(title)
        if book:
            self.__books.remove(book)

    def issue_book(self, title: str) -> bool:
        book = self.find_book(title)
        if book and book.issue():
            return True
        return False

    def return_book(self, title: str):
        book = self.find_book(title)
        if book:
            book.return_book()


# Автотесты
if __name__ == "__main__":
    # Создаем библиотеку
    library = Library()

    # Добавляем книги
    book1 = Book("1984", "Джордж Оруэлл", 1949, "Антиутопия")
    library.add_book(book1)

    ebook1 = EBook("Преступление и наказание", "Федор Достоевский", 1866, "Роман", "PDF")
    library.add_book(ebook1)

    # Поиск книги
    found_book = library.find_book("1984")
    assert found_book is not None, "Книга не найдена."

    # Выдача книги
    assert library.issue_book("1984"), "Книга должна быть выдана."
    assert not library.issue_book("1984"), "Книга уже на руках."

    # Возврат книги
    library.return_book("1984")
    assert library.issue_book("1984"), "Книга должна быть выдана снова."

    # Удаление книги
    library.remove_book("1984")
    assert library.find_book("1984") is None, "Книга должна быть удалена."
    print("Все тесты пройдены успешно.")
