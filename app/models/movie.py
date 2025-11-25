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
    @property
    def genres_id(self):
        return self._genres_id
    @property
    def director(self):
        return self._director
    @property
    def release_year(self):
        return self._release_year
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
