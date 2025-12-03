from abc import ABC, abstractmethod
from app.models.user import User
class RecommendationStrategy(ABC):
    def __init__(self, user:User):
        self.user = user
    @abstractmethod
    def get_recommendations(self, user):
        pass

#Использовать это:
class RecommendationSystem:
    def __init__(self,user:User, strategy: RecommendationStrategy):
        self.strategy = strategy(user)

    def set_strategy(self, strategy: RecommendationStrategy):
        self.strategy = strategy

    def recommend(self, user):
        return self.strategy.get_recommendations(user)