'''  - Класс "Пользователь" с атрибутами: идентификатор, имя, список просмотренных фильмов с оценками, предпочтительные жанры'''

class User():
    def __init__(self, id,nickname,movie_history_with_raiting:dict,id_preferred_genres:list):
        self.__id = id
        self.__nickname = nickname
        self.__movie_history_with_raiting = movie_history_with_raiting
        self.__id_preferred_genres = id_preferred_genres

    @property
    def id(self):
        return self.__id
    @property
    def nickname(self):
        return self.__nickname
    @property
    def movie_history_with_raiting(self):
        return self.__movie_history_with_raiting
    @property
    def id_preferred_genres(self):
        return self.__id_preferred_genres

    def add_id_preferred_genres(self, id_preferred_genres:list):

        self.__id_preferred_genres.extend(id_preferred_genres)

    def add_movie_history_with_raiting(self, movie_id:int,raiting:float):
        if 0 <= raiting <= 10:
            self.__movie_history_with_raiting[movie_id] = raiting
        else:
            raise ValueError("Рейтинг должен быть от 0 до 10")

