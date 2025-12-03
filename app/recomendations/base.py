from abc import ABC, abstractmethod

class RecommendationStrategy(ABC):
    @abstractmethod
    def get_recommendations(self, user):
        pass

#Использовать это:
class RecommendationSystem:
    def __init__(self, strategy: RecommendationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: RecommendationStrategy):
        self.strategy = strategy

    def recommend(self, user):
        return self.strategy.get_recommendations(user)