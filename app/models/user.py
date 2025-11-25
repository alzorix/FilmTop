'''  - Класс "Пользователь" с атрибутами: идентификатор, имя, список просмотренных фильмов с оценками, предпочтительные жанры'''

class User():
    def __init__(self, id: int, nickname: str, movie_history_with_rating: dict = None,
                 preferred_genres: list = None):
        self.__id = id
        self.__nickname = nickname
        self.__movie_history_with_rating = movie_history_with_rating or {}
        self.__preferred_genres = preferred_genres or []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, value: str):
        if not value:
            raise ValueError("Имя не может быть пустым")
        self.__nickname = value

    @property
    def movie_history_with_rating(self) -> dict:
        return self.__movie_history_with_rating

    @property
    def preferred_genres(self) -> list:
        return self.__preferred_genres

    def add_preferred_genres(self, genre_ids: list):
        for g_id in genre_ids:
            if g_id not in self.__preferred_genres:
                self.__preferred_genres.append(g_id)

    def  add_movie_history(self, movie_id: str, rating: float):
        if (0 <= rating <= 10):
            self.__movie_history_with_rating[str(movie_id)] = rating
        else:

            raise ValueError("Rating must be between 0 and 10")

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "nickname": self.__nickname,
            "movie_history_with_rating": self.__movie_history_with_rating,
            "preferred_genres": self.__preferred_genres
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"],
                   data["nickname"],
                   data.get("movie_history_with_rating",{}),
                   data.get("preferred_genres", []))

