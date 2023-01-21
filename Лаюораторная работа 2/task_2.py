from task_1 import Book, BOOKS_DATABASE


class Library:
    """ Класс библиотека
    """
    def __init__(self, books: list[Book] = None):
        """
        :param books: список книг
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """
        Получение индентификатора для добавления новой книги в библиотеку

        :return: id для новой книги
        """
        if len(self.books) == 0:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_):
        """
        Получение индекса книги в списке книг библиотеки по ее индентификатору

        :param id_: индентификатор требуемой книги
        :return: индекс книги в списке
        """
        for index, book in enumerate(self.books):
            if book.id_ == id_:
                return index
        raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
