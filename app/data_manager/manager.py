import json
from abc import ABC, abstractmethod

from app.models.genre import Genre

from app.models.user import User

from app.models.movie import Movie

user_data_path = "../../data/user_data.json"
genre_data_path = "../../data/genre_data.json"
movie_data_path = "../../data/movie_data.json"

class Data_File_Worker(ABC):
    def __init__(self, filename):
        self._file_path = filename

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass


class Json_File_Worker(Data_File_Worker):
    def __init__(self, json_file):
        super().__init__(json_file)

    def read_data(self):
        try:
            with open(self._file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл не найден")
            return {}
    def write_data(self, data: dict):
        #Проще говоря,берём наш список и приводим к виду: id: класс в виде словаря. Если класс уже словарь- не трогаем
        temp_dict = {}
        for key, value in data.items():
            if hasattr(value, "to_dict"):
                temp_dict[str(key)] = value.to_dict()
            else:
                temp_dict[str(key)] = value
        with open(self._file_path, 'w', encoding='utf-8') as f:
            json.dump(temp_dict, f)

class Data_Manager(ABC):
    def __init__(self, data_path,data_manager:Data_File_Worker,cls): #data_manager - это класс,внутри создаётся объект
        self._data_path = data_path
        self._data_= None
        self.manager = data_manager(self._data_path)
        self._cls = cls  # Класс объекта (User, Movie, Genre)
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def update(self,det):
        pass

    #Реализация по идеи одинаковая
    def remove(self, id):
        data = self.manager.read_data()
        str_id = str(id)
        if str_id in data:
            data.pop(str_id)
            self.manager.write_data(data)
        else:
            raise KeyError(f"ID {id} не найден")
    def read_all_data(self): # Если в моём коде лень разбираться - получаете данные и работаете с ними как хотите.
        return self.manager.read_data()

    def hard_write_data(self, data: dict):
        # Если в моём коде лень разбираться - После  read_all_data изменённый словарь кидаете сюда
        #По идеи должно работать
        """
        Универсальный метод записи словаря в файл.
        data: словарь, где ключи — ID, значения — объекты User или словари
        """
        self.manager.write_data(data)

    def get_data_for_index(self, index):
        data = self.manager.read_data()
        key = str(index)
        item = data.get(key)
        if item is None:
            raise KeyError(f"ID {index} не найден")
        # Делаем точно класс
        if isinstance(item, dict):
            return self._cls.from_dict(item)
        return item



class User_Manager(Data_Manager):
    def __init__(self, data_path=user_data_path, data_manager:Data_File_Worker=Json_File_Worker):
        #  В data_manager нужно передавать класс,не обьект класса.
        super().__init__(data_path, data_manager,User)

    def add(self, nickname: str, movie_history=None, preferred_genres=None) -> User:

        movie_history = movie_history or {}
        preferred_genres = preferred_genres or []

        data = self.manager.read_data() or {}

        # Определяем новый ID: максимум существующих + 1
        if data:
            new_id = max(int(k) for k in data.keys()) + 1
        else:
            new_id = 1

        new_user = User(new_id, nickname, movie_history, preferred_genres)


        data[str(new_id)] = new_user


        self.manager.write_data(data)

        return new_user

    def update(self, id, nickname=None, movie_history=None, preferred_genres=None) -> User:
        data = self.manager.read_data()
        str_id = str(id)
        if str_id not in data:
            raise KeyError(f"Такого ID не существует")

        user_data = data[str_id]
        user = User.from_dict(user_data) if isinstance(user_data, dict) else user_data

        if nickname is not None:
            user.nickname = nickname
        if movie_history is not None:
            for m_id, rating in movie_history.items():
                user.add_movie_history(m_id, rating)
        if preferred_genres is not None:
            user.add_preferred_genres(preferred_genres)
        data[str_id] = user
        self.manager.write_data(data)
        return user


class Genre_Manager(Data_Manager):
    def __init__(self, data_path=genre_data_path, data_manager=Json_File_Worker):
        super().__init__(data_path, data_manager,Genre)

    def add(self, movie_name):
        data = self.manager.read_data() or {}

        # Определяем новый ID: максимум существующих + 1
        if data:
            new_id = max(int(k) for k in data.keys()) + 1
        else:
            new_id = 1
        new_genre = Genre(new_id, movie_name)
        data[str(new_id)] = new_genre
        self.manager.write_data(data)
        return new_genre

    def update(self, id, name):
        data = self.manager.read_data()
        str_id = str(id)
        if str_id not in data:
            raise KeyError(f"Такого ID не существует")
        genre_data = data[str_id]
        genre = Genre.from_dict(genre_data) if isinstance(genre_data, dict) else genre_data
        genre.name = name
        data[str_id] = genre
        self.manager.write_data(data)
        return genre




class Movie_Manager(Data_Manager):
    def __init__(self, data_path=movie_data_path, data_manager=Json_File_Worker):
        super().__init__(data_path, data_manager,Movie)
    def add(self, movie_name,genres_id,director,release_year):
        data = self.manager.read_data() or {}

        # Определяем новый ID: максимум существующих + 1
        if data:
            new_id = max(int(k) for k in data.keys()) + 1
        else:
            new_id = 1
        new_movie = Movie(new_id, movie_name,genres_id,director,release_year)
        data[str(new_id)] = new_movie
        self.manager.write_data(data)
        return new_movie
    def update(self, id, title=None, genres_id=None, director=None, release_year=None):
        data = self.manager.read_data()
        str_id = str(id)
        if str_id not in data:
            raise KeyError(f"Такого ID не существует")
        movie_data = data[str_id]
        movie = Movie.from_dict(movie_data) if isinstance(movie_data, dict) else movie_data

        if title is not None:
            movie.title = title
        if genres_id is not None:
            movie._genres_id = genres_id
        if director is not None:
            movie.director = director
        if release_year is not None:
            movie.release_year = release_year

        data[str_id] = movie
        self.manager.write_data(data)
        return movie

#Выборочная проверка работоспособности
# user_managa = User_manager()
# test = user_managa.add("Petya",{1:8.00},[1,2])
# user_managa.remove(test.id-1)
#
# genre_managa = Genre_manager()
# test_genre = genre_managa.add("Petya")
# test_genre = genre_managa.read_all_data()
# print(test_genre)
#
# movie_managa = Movie_manager()
# test_movie = movie_managa.add("Petya",{"1":100},"Пушкин",release_year=1999)
# test_movie = movie_managa.read_all_data()
# print(test_movie)
