
class Genre:
    def __init__(self, id: int, name: str):
        self._id = id
        if not name:
            raise ValueError("Genre name cannot be empty")
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Genre name cannot be empty")
        self._name = value

    def to_dict(self) -> dict:
        return {"id": self._id, "name": self._name}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["name"]) #Восстанавливаем класс из словаря

    def __repr__(self):
        return f"Genre(id={self._id}, name='{self._name}')"