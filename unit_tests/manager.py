#На всякий случай unittest-ы от chatgpt
import pytest
import json
from app.models.user import User
from app.models.movie import Movie
from app.models.genre import Genre
from app.data_manager.manager import Json_File_Worker, User_Manager, Movie_Manager, Genre_Manager

# ====== Вспомогательная функция ======
def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f)


# ====== UserManager tests ======
def test_user_manager_get_data_for_index(tmp_path):
    # Создаём временный файл
    file_path = tmp_path / "users.json"
    # Пишем тестовые данные (словари)
    user_data = {
        "1": {"id": 1, "nickname": "Alice", "movie_history": {}, "preferred_genres": []},
        "2": {"id": 2, "nickname": "Bob", "movie_history": {}, "preferred_genres": []}
    }
    write_json(file_path, user_data)

    # Создаём UserManager
    manager = User_Manager(data_path=str(file_path))

    # Проверяем, что метод возвращает объект User
    user = manager.get_data_for_index(1)
    assert isinstance(user, User)
    assert user.id == 1
    assert user.nickname == "Alice"

    # Проверяем KeyError для несуществующего ID
    with pytest.raises(KeyError):
        manager.get_data_for_index(999)


# ====== MovieManager tests ======
def test_movie_manager_get_data_for_index(tmp_path):
    file_path = tmp_path / "movies.json"
    movie_data = {
        "1": {"id": 1, "title": "Movie1", "genres_id": [1], "director": "Director1", "release_year": 2000}
    }
    write_json(file_path, movie_data)

    manager = Movie_Manager(data_path=str(file_path))
    movie = manager.get_data_for_index(1)
    assert isinstance(movie, Movie)
    assert movie.title == "Movie1"


# ====== GenreManager tests ======
def test_genre_manager_get_data_for_index(tmp_path):
    file_path = tmp_path / "genres.json"
    genre_data = {
        "1": {"id": 1, "name": "Action"}
    }
    write_json(file_path, genre_data)

    manager = Genre_Manager(data_path=str(file_path))
    genre = manager.get_data_for_index(1)
    assert isinstance(genre, Genre)
    assert genre.name == "Action"
