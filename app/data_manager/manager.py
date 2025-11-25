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
        with open(self._file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

    def write_data(self, data: dict):
        #Проще говоря,берём наш список и приводим к виду: id: класс в виде словаря. Если класс уже словарь- не трогаем
        temp_dict = {str(key): class_data.__dict__ if (isinstance(class_data, User) or  isinstance(class_data, Movie) or isinstance(class_data, Genre) )  else class_data for key, class_data in data.items()}
        with open(self._file_path, 'w', encoding='utf-8') as outfile:
            json.dump(temp_dict, outfile)


class Data_Manager(ABC):
    def __init__(self, data_path,data_manager:Data_File_Worker): #data_manager - это класс,внутри создаётся объект
        self._data_path = data_path
        self._data_= None
        self.manager = data_manager(self._data_path)
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def update(self,det):
        pass

    #Реализация по идеи одинаковая
    def remove(self,id:int):
        data = self.manager.read_data() or {}
        data.pop(str(id))
        self.manager.write_data(data)
    def read_all_data(self):
        return self.manager.read_data()

    def get_data_for_index(self, index):
        data = self.manager.read_data() or {}
        if data == {}:
            raise KeyError("Data not found")
        return data[str(index)]

class User_manager(Data_Manager):
    def __init__(self, data_path=user_data_path, data_manager:Data_File_Worker=Json_File_Worker):
        #  В data_manager нужен класс
        super().__init__(data_path, data_manager)

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

    def update(self, id: int, nickname: str = None, movie_history: dict = None, preferred_genres: list = None):

        data = self.manager.read_data() or {}
        str_id = str(id)
        if str_id not in data:
            raise KeyError(f"User with ID {id} not found")
        user = data[str_id]
        if nickname is not None:
            user.nickname = nickname
        if movie_history is not None:
            user.movie_history = movie_history
        if preferred_genres is not None:
            user.preferred_genres = preferred_genres
        data[str_id] = user
        self.manager.write_data(data)
        return user


class Genre_manager(Data_Manager):
    def __init__(self, data_path=genre_data_path, data_manager=Json_File_Worker):
        super().__init__(data_path, data_manager)

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

    def update(self, id: int, genre_name: str):
        data = self.manager.read_data() or {}
        str_id = str(id)
        if str_id not in data:
            raise KeyError(f"Genre with ID {id} not found")
        genre = data[str_id]
        genre.genre_name = genre_name
        data[str_id] = genre
        self.manager.write_data(data)
        return genre




class Movie_manager(Data_Manager):
    def __init__(self, data_path=movie_data_path, data_manager=Json_File_Worker):
        super().__init__(data_path, data_manager)
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
    def update(self, id: int, movie_name: str):

        data = self.manager.read_data() or {}
        str_id = str(id)
        if str_id not in data:
            raise KeyError(f"Movie with ID {id} not found")
        movie = data[str_id]
        movie.movie_name = movie_name
        data[str_id] = movie
        self.manager.write_data(data)
        return movie


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
