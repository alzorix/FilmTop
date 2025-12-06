from app.recomendations.base import RecommendationStrategy
from app.models.user import User
from app.data_manager.manager import Movie_Manager,User_Manager

class GenreRecommendationStrategy(RecommendationStrategy):
    def __init__(self,user:User):
        super().__init__(user)
        self.movie_manager = Movie_Manager()
    def get_recommendations(self):
        recommend_movie_id = set()
        movie_history_with_rating = self.user.movie_history_with_rating
        preferred_genres = self.user.preferred_genres
        movies_data = self.movie_manager.read_all_data_as_class()

        for movie in movies_data:
            if str(movie.id) not in movie_history_with_rating.keys():
                for current_genre_id in preferred_genres:
                    if current_genre_id in movie.genres_id:
                        recommend_movie_id.add(movie.id)
        return recommend_movie_id



# test = User_Manager().get_data_for_index(1)
#
# print(test.preferred_genres)
# print(test.movie_history_with_rating)
# test1 = GenreRecommendationStrategy(test)
# print(test1.get_recommendations())

