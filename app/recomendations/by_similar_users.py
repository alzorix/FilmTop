from app.recomendations.base import RecommendationStrategy
from app.models.user import User
from app.data_manager.manager import User_Manager


class SimilarUsersRecommendationStrategy(RecommendationStrategy):
    def __init__(self,user:User):
        super().__init__(user)
        self.user_manager = User_Manager()
    def get_recommendations(self):
        recommend_movie_id = set()
        movie_history_with_rating = self.user.movie_history_with_rating
        preferred_genres = self.user.preferred_genres
        users_data = self.user_manager.read_all_data_as_class()
        matches = 0
        total = set()

        for other_user in users_data:
            for genre in preferred_genres:
                for another_preference in other_user.preferred_genres:
                    total.add(another_preference)
                    if genre == another_preference:
                        matches += 1
            if matches/len(preferred_genres) > 0.5:
                for id in other_user.movie_history_with_rating.keys():
                    if str(id) not in movie_history_with_rating.keys():
                        recommend_movie_id.add(id)
        return recommend_movie_id