class User:

    def __init__(self, id: int, nickname: str, movie_history_with_rating: dict = None,
                 preferred_genres: list = None):
        """
        Инициализация пользователя.

        Args:
            id (int): Уникальный идентификатор.
            nickname (str): Никнейм пользователя.
            movie_history_with_rating (dict, optional): История просмотров с рейтингами.
            preferred_genres (list, optional): Список id предпочтительных жанров.
        """
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
        """Словарь просмотренных фильмов с рейтингами."""
        return self.__movie_history_with_rating

    @property
    def preferred_genres(self) -> list:
        """Список id предпочтительных жанров."""
        return self.__preferred_genres

    def add_preferred_genres(self, genre_ids: list):
        """Добавляет жанры в предпочтения, исключая дубликаты."""
        for g_id in genre_ids:
            if g_id not in self.__preferred_genres:
                self.__preferred_genres.append(g_id)

    def add_movie_history(self, movie_id: str, rating: float):
        """
        Добавляет фильм с рейтингом в историю просмотров.

        Args:
            movie_id (str): Идентификатор фильма.
            rating (float): Рейтинг от 0 до 10.

        Raises:
            ValueError: Если рейтинг не в диапазоне 0-10.
        """
        if 0 <= rating <= 10:
            self.__movie_history_with_rating[str(movie_id)] = rating
        else:
            raise ValueError("Рейтинг должен быть 0 до 10")

    def to_dict(self) -> dict:
        """Возвращает данные пользователя в виде словаря."""
        return {
            "id": self.__id,
            "nickname": self.__nickname,
            "movie_history_with_rating": self.__movie_history_with_rating,
            "preferred_genres": self.__preferred_genres
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Создает пользователя из словаря."""
        return cls(
            data["id"],
            data["nickname"],
            data.get("movie_history_with_rating", {}),
            data.get("preferred_genres", [])
        )
