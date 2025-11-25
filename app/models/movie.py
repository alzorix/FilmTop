# Класс
# "Фильм" с атрибутами: идентификатор, название, жанры, режиссер, год выпуска, рейтинг


class Movie():
    def __init__(self, id:int,title:str,genres_id:list,director:str,release_year:int,rating:float = 0.0,rating_count:int = 0):
        self._id = id
        self._title = title
        self._genres_id = genres_id
        self._director = director
        self._release_year = release_year
        self._rating = rating
        self._rating_count = rating_count
    def __str__(self):
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
        return self._rating
    @rating.setter
    def rating(self, value):
        if 0 <= value <= 10:
            self._rating = value
        else:
            raise ValueError("Рейтинг должен быть от 0 до 10")
    def add_rating(self, value:float): #метод для пользователя: пользователь ставит оценку свою,и общая оценка тоже изменяется
        if 0 <= value <= 10:
            current_rating = self._rating
            current_rating_count = self._rating_count
            self._rating = (current_rating*current_rating_count + value) /(current_rating_count +1)
            #(Восстановленная сумма оценок + текущая )/ на число оценок с учётом новой оценки
            self._rating_count +=1
        else:
            raise ValueError("Рейтинг должен быть от 0 до 10")

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "title": self._title,
            "genres_id": self._genres_id,
            "director": self._director,
            "release_year": self._release_year,
            "rating": self._rating,
            "rating_count": self._rating_count
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["id"], data["title"], data["genres_id"], data["director"],
            data["release_year"], data.get("rating", 0.0), data.get("rating_count", 0)
        )
