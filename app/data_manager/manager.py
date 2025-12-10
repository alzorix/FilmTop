import json
from abc import ABC, abstractmethod

from app.models.genre import Genre

from app.models.user import User

from app.models.movie import Movie

import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
DATA_DIR = "data"
user_data_path = os.path.join(DATA_DIR, "user_data.json")
movie_data_path = os.path.join(DATA_DIR, "movie_data.json")
genre_data_path = os.path.join(DATA_DIR, "genre_data.json")

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
            print("Файл не найден, вернем пустой словарь")
            return {}

    def write_data(self, data: dict):
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)

        temp_dict = {}
        for key, value in data.items():
            if hasattr(value, "to_dict"):
                temp_dict[str(key)] = value.to_dict()
            else:
                temp_dict[str(key)] = value

        with open(self._file_path, 'w', encoding='utf-8') as f:
            json.dump(temp_dict, f, indent=4)


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

    def read_all_data_as_class(self):
        data = self.manager.read_data()
        data = list([data.get(elem) for elem in data])
        data = [(lambda elem: self._cls.from_dict(elem))(elem) for elem in data]
        return data

    def hard_write_data(self, data: dict):
        # Если в моём коде лень разбираться - После  read_all_data изменённый словарь кидаете сюда
        #По идеи должно работать
        """
        Универсальный метод записи словаря в файл.
        data: словарь, где ключи — ID, значения — объекты User или словари
        """
        self.manager.write_data(data)

    def get_class_for_index(self, index):

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

    def update(self, user:User) -> User:
        data = self.manager.read_data()
        str_id = str(user.id)
        if str_id not in data:
            raise KeyError(f"Такого ID не существует")
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

    def update(self, genre:Genre) -> Genre:
        data = self.manager.read_data()
        str_id = str(genre.id)
        if str_id not in data:
            raise KeyError(f"Такого ID не существует")
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

    def update(self, movie:Movie) -> Movie:
        data = self.manager.read_data()
        str_id = str(movie.id)
        if str_id not in data:
            raise KeyError(f"Такого ID не существует")
        data[str_id] = movie
        self.manager.write_data(data)
        return movie

#Выборочная проверка работоспособности/тестовая база
# user_managa = User_Manager()
# test = user_managa.add("Alexander",{1:8.00},[1,2])
# test = user_managa.add("Amir",{1:1.00,2:10.00,3:10.00},[1,2,3])
# #user_managa.remove(test.id-1)
# print(user_managa.read_all_data())
# genre_managa = Genre_Manager()
# test_genre = genre_managa.add("Боевик")
# test_genre = genre_managa.add("Драма")
# test_genre = genre_managa.add("Комедия")
# test_genre = genre_managa.read_all_data()
# print(test_genre)
#
# movie_managa = Movie_Manager()
# test_movie = movie_managa.add("Война и Мир",[2],"Советский чел",release_year=1980)
# test_movie = movie_managa.add("Американский Солдат",[1,3],"Американский чел",release_year=2002)
# test_movie = movie_managa.add("Путешествия Ивана",[1,2,3],"Иван",release_year=2025)
# test_movie = movie_managa.read_all_data()
# print(test_movie)
