from app.recomendations.base import RecommendationStrategy
from app.models.user import User
from app.data_manager.manager import Movie_Manager,User_Manager


class RatingRecommendationStrategy(RecommendationStrategy):
    def __init__(self,user:User):
        super().__init__(user)
        self.movie_manager = Movie_Manager()
    def get_recommendations(self, ratingStart=7, ratingTop=10):
        recommend_movie_id = set()
        movie_history_with_rating = self.user.movie_history_with_rating
        movies_data = self.movie_manager.read_all_data_as_class()

        for movie in movies_data:
            if ratingStart <= movie.rating <= ratingTop:
                if str(movie.id) not in movie_history_with_rating.keys():
                    recommend_movie_id.add(movie.id)
        return recommend_movie_id