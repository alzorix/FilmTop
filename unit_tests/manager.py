import pytest
from app.data_manager.manager import Json_File_Worker, User_Manager, Genre_Manager, Movie_Manager
from app.models.user import User
from app.models.genre import Genre
from app.models.movie import Movie


# Fixtures для временных файлов

@pytest.fixture
def user_file(tmp_path):
    file = tmp_path / "user.json"
    file.write_text("{}", encoding="utf-8")
    return str(file)

@pytest.fixture
def genre_file(tmp_path):
    file = tmp_path / "genre.json"
    file.write_text("{}", encoding="utf-8")
    return str(file)

@pytest.fixture
def movie_file(tmp_path):
    file = tmp_path / "movie.json"
    file.write_text("{}", encoding="utf-8")
    return str(file)

def test_user_add(user_file):
    manager = User_Manager(data_path=user_file, data_manager=Json_File_Worker)
    u = manager.add("Alex", {1: 8}, [1, 2])
    assert isinstance(u, User)
    assert u.id == 1
    assert u.nickname == "Alex"
    data = manager.read_all_data()
    assert "1" in data
    assert data["1"]["nickname"] == "Alex"

def test_user_add_multiple_ids(user_file):
    manager = User_Manager(data_path=user_file, data_manager=Json_File_Worker)
    u1 = manager.add("Alex")
    u2 = manager.add("Max")
    assert u1.id == 1
    assert u2.id == 2

def test_user_update(user_file):
    manager = User_Manager(data_path=user_file, data_manager=Json_File_Worker)
    u = manager.add("Alex")
    u.nickname = "NewName"
    manager.update(u)
    data = manager.read_all_data()
    assert data["1"]["nickname"] == "NewName"

def test_user_remove(user_file):
    manager = User_Manager(data_path=user_file, data_manager=Json_File_Worker)
    u = manager.add("Alex")
    manager.remove(u.id)
    data = manager.read_all_data()
    assert data == {}

def test_user_get_by_id(user_file):
    manager = User_Manager(data_path=user_file, data_manager=Json_File_Worker)
    manager.add("Alex")
    user_obj = manager.get_class_for_index(1)
    assert isinstance(user_obj, User)
    assert user_obj.nickname == "Alex"


def test_genre_add(genre_file):
    manager = Genre_Manager(data_path=genre_file, data_manager=Json_File_Worker)
    g = manager.add("Action")
    assert isinstance(g, Genre)
    assert g.id == 1
    data = manager.read_all_data()
    assert data["1"]["name"] == "Action"

def test_genre_update(genre_file):
    manager = Genre_Manager(data_path=genre_file, data_manager=Json_File_Worker)
    g = manager.add("Action")
    g.name = "Adventure"
    manager.update(g)
    data = manager.read_all_data()
    assert data["1"]["name"] == "Adventure"


def test_movie_add(movie_file):
    manager = Movie_Manager(data_path=movie_file, data_manager=Json_File_Worker)
    m = manager.add("Alien", [1], "Ridley", 1979)
    assert isinstance(m, Movie)
    assert m._id == 1
    data = manager.read_all_data()
    assert data["1"]["title"] == "Alien"

def test_movie_update(movie_file):
    manager = Movie_Manager(data_path=movie_file, data_manager=Json_File_Worker)
    m = manager.add("Alien", [1], "Ridley", 1979)
    m._title = "Alien 2"
    manager.update(m)
    data = manager.read_all_data()
    assert data["1"]["title"] == "Alien 2"