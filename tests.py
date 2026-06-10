import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже

    # 1. Тест добавления книг с валидными названиями (длина от 1 до 40)
    @pytest.mark.parametrize("book_name", ["Обычная книга", "A" * 1, "B" * 40])
    def test_add_new_book_valid(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    # 2. Тест, что книга с невалидным названием не добавляется
    @pytest.mark.parametrize("invalid_name", ["", "C" * 41])
    def test_add_new_book_invalid_name(self, invalid_name):
        collector = BooksCollector()
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    # 3. Тест установки жанра для существующей книги
    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Фантастика")
        assert collector.get_book_genre("Книга") == "Фантастика"

    # 4. Тесты, что жанр не устанавливается для несуществующей книги или недопустимого жанра
    @pytest.mark.parametrize("book_name, genre", [("Несуществующая", "Фантастика"), ("Существующая", "Нежанр")])
    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_new_book("Существующая книга")
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert collector.get_book_genre("Несуществующая книга") is None

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Существующая книга")
        collector.set_book_genre("Существующая книга", "Нежанр")
        assert collector.get_book_genre("Существующая книга") == ""

    # 5. Тест получения списка книг по конкретному жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Ужасная книга")
        collector.add_new_book("Детективчик")
        collector.add_new_book("Фантастика")
        collector.set_book_genre("Ужасная книга", "Ужасы")
        collector.set_book_genre("Детективчик", "Детективы")
        collector.set_book_genre("Фантастика", "Фантастика")
        horror_books = collector.get_books_with_specific_genre("Ужасы")
        assert horror_books == ["Ужасная книга"]

    # 6. Тест, что метод возвращает только книги без возрастного рейтинга
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Для детей")
        collector.add_new_book("Ужасы")
        collector.add_new_book("Комедия")
        collector.set_book_genre("Для детей", "Мультфильмы")
        collector.set_book_genre("Ужасы", "Ужасы")
        collector.set_book_genre("Комедия", "Комедии")
        children_books = collector.get_books_for_children()
        assert children_books == ["Для детей", "Комедия"]

    # 7. Тест добавления книги в избранное и отсутствие дублей
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        assert collector.get_list_of_favorites_books() == ["Любимая книга"]

    # 8. Тест удаления книги из избранного и удаление отсутствующей не ломает
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        collector.delete_book_from_favorites("Нет такой")
        assert collector.get_list_of_favorites_books() == []

    # 9. Тест, что изначально список избранных книг пуст
    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
