from app.recomendations.base import RecommendationStrategy
from app.models.user import User
from app.data_manager.manager import User_Manager


class SimilarUsersRecommendationStrategy(RecommendationStrategy):
    def __init__(self, user: User):
        super().__init__(user)
        self.user_manager = User_Manager()

    def get_recommendations(self):
        recommend_movie_id = set()
        current_user_movie_history_with_rating = self.user.movie_history_with_rating
        user_preferred_genres = self.user.preferred_genres
        users_data = self.user_manager.read_all_data_as_class()
        matches = 0

        if len(user_preferred_genres) == 0 and len(current_user_movie_history_with_rating) == 0:
            return set()

        for other_user in users_data:
            if other_user.id == self.user.id:
                continue

            genre_matches = 0
            movie_matches = 0
            other_user_movie_history = other_user.movie_history_with_rating

            for genre in user_preferred_genres:
                for another_preference in other_user.preferred_genres:
                    if genre == another_preference:
                        genre_matches += 1
            
            for mid, movie_rating in self.user.movie_history_with_rating.items():
                for other_mid,other_movie_rating in other_user_movie_history:
                    if mid == other_mid:
                        if movie_rating - other_movie_rating <= 1:
                            movie_matches += 1

            
            if genre_matches > 0:
                if genre_matches/len(user_preferred_genres) > 0.5:
                    for mid, rating in other_user_movie_history.items():
                        if rating > 7:
                            if str(mid) not in current_user_movie_history_with_rating.keys():
                                recommend_movie_id.add(mid)
            elif movie_matches > 0:
                if movie_matches/len(current_user_movie_history_with_rating) > 0.2:
                    for mid, rating in other_user_movie_history.items():
                        if rating > 7:
                            if str(mid) not in current_user_movie_history_with_rating.keys():
                                recommend_movie_id.add(mid)

        return recommend_movie_id
