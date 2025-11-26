class Movie:
    """
    Класс, представляющий фильм с базовыми характеристиками: названием, режиссёром,
    жанрами, годом выпуска и рейтингом.

    Атрибуты:
        id (int): Уникальный идентификатор фильма.
        title (str): Название фильма.
        genres_id (list[int]): Список идентификаторов жанров.
        director (str): Имя режиссёра.
        release_year (int): Год выпуска (допустимый диапазон: 1800–2100).
        rating (float): Средний рейтинг фильма (от 0 до 10).
        rating_count (int): Количество выставленных оценок.
    """

    def __init__(self, id: int, title: str, genres_id: list,
                 director: str, release_year: int,
                 rating: float = 0.0, rating_count: int = 0):
        self._id = id
        self._title = title
        self._genres_id = genres_id
        self._director = director
        self._release_year = release_year
        self._rating = rating
        self._rating_count = rating_count

    def __str__(self):
        """Возвращает строковое представление фильма в формате 'Название (Год) — Рейтинг/10'."""
        return f"{self._title} ({self._release_year}) - {self._rating}/10"

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title: str):
        if not new_title:
            raise ValueError("Поле не может быть пустым")
        self._title = new_title

    @property
    def genres_id(self):
        return self._genres_id

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, new_director: str):
        if not new_director:
            raise ValueError("Поле не может быть пустым")
        self._director = new_director

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, value: int):
        if value < 1800 or value > 2100:
            raise ValueError("Неверный год выпуска")
        self._release_year = value

    @property
    def rating(self):
        """float: Средний рейтинг фильма (0–10)."""
        return self._rating

    @rating.setter
    def rating(self, new_rating: float):
        """
        Устанавливает рейтинг фильма.

        Args:
            new_rating (float): Новый рейтинг.

        Raises:
            ValueError: Если значение не в диапазоне 0–10.
        """
        if 0 <= new_rating <= 10:
            self._rating = new_rating
        else:
            raise ValueError("Рейтинг должен быть от 0 до 10")

    @property
    def rating_count(self) -> int:
        """Возвращает количество отзывов."""
        return self._rating_count

    @rating_count.setter
    def rating_count(self, new_rating_count: int):
        """
        Устанавливает количество отзывов.

        Args:
            new_rating_count (int): Новое количество отзывов.

        Raises:
            ValueError: Если значение отрицательное.
        """
        if new_rating_count >= 0:
            self._rating_count = new_rating_count
        else:
            raise ValueError("Число отзывов должно быть неотрицательным.")


    def add_rating(self, value: float):
        """
        Добавляет новую пользовательскую оценку и пересчитывает средний рейтинг.

        Формула:
            new_rating = (текущий_рейтинг * количество + новая_оценка) / (количество + 1)

        Args:
            value (float): Новая оценка (0–10).

        Raises:
            ValueError: Если значение не в допустимом диапазоне.
        """
        if 0 <= value <= 10:
            current_rating = self._rating
            current_rating_count = self._rating_count
            self._rating = (current_rating * current_rating_count + value) / (current_rating_count + 1)
            self._rating_count += 1
        else:
            raise ValueError("Рейтинг должен быть от 0 до 10")

    def to_dict(self) -> dict:
        """
        Преобразует объект фильма в словарь.

        Returns:
            dict: Словарь с данными фильма.
        """
        return {
            "id": self._id,
            "title": self._title,
            "genres_id": self._genres_id,
            "director": self._director,
            "release_year": self._release_year,
            "rating": self._rating,
            "rating_count": self._rating_count,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Создаёт объект Movie из словаря данных.

        Args:
            data (dict): Данные о фильме.

        Returns:
            Movie: Новый объект класса.
        """
        return cls(
            data["id"], data["title"], data["genres_id"], data["director"],
            data["release_year"], data.get("rating", 0.0), data.get("rating_count", 0)
        )
