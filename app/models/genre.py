class Genre:
    def __init__(self, id: int, name: str):
        """
        Инициализация жанра.

        Args:
            id (int): Уникальный идентификатор жанра.
            name (str): Название жанра.

        Raises:
            ValueError: Если имя пустое.
        """
        self._id = id
        if not name:
            raise ValueError("Имя не может быть пустым")
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        """Устанавливает название жанра."""
        if not value:
            raise ValueError("Имя не может быть пустым")
        self._name = value

    def to_dict(self) -> dict:
        """Возвращает класс в виде словаря."""
        return {"id": self._id, "name": self._name}

    @classmethod
    def from_dict(cls, data: dict):
        """Создает класс из словаря."""
        return cls(data["id"], data["name"])

    def __repr__(self):
        return f"Genre(id={self._id}, name='{self._name}')"
