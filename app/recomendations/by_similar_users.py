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
        preferred_genres = self.user.preferred_genres
        users_data = self.user_manager.read_all_data_as_class()
        matches = 0

        if len(preferred_genres) == 0 and len(current_user_movie_history_with_rating) == 0:
            return set()

        for other_user in users_data:
            other_user_liked_films = []

            if other_user.id == self.user.id:
                continue

            matches = 0

            for genre in preferred_genres:
                for another_preference in other_user.preferred_genres:
                    if genre == another_preference:
                        matches += 1
            
            for movie_id in current_user_movie_history_with_rating.keys():
                if current_user_movie_history_with_rating[movie_id] > 7:
                    for other_movie_id in other_user.movie_history_with_rating.keys():
                        if movie_id == other_movie_id and other_user.movie_history_with_rating[other_movie_id]:
                            matches += 1
                            other_user_liked_films.append(other_movie_id)

            if (matches / (len(preferred_genres)+len([mov for mov in current_user_movie_history_with_rating if float(usrecs.user.movie_history_with_rating[mov]) > 7.0]))) > 0.5:
                for mid in other_user_liked_films:
                    if str(mid) not in current_user_movie_history_with_rating.keys():
                        recommend_movie_id.add(mid)

        return recommend_movie_id