from app.data_manager.manager import User_Manager, Movie_Manager
from app.models.user import User
from app.recomendations.be_genre import GenreRecommendationStrategy
from app.recomendations.by_rating import RatingRecommendationStrategy
from app.recomendations.by_similar_users import SimilarUsersRecommendationStrategy

class UserService:
    def __init__(self):
        self.user_manager = User_Manager()
        self.movie_manager = Movie_Manager()

    def register_user(self, nickname: str) -> User:
        return self.user_manager.add(nickname)

    def login_user(self, user_id: int) -> User:
        try:
            return self.user_manager.get_class_for_index(user_id)
        except KeyError:
            print("Пользователь не найден")
            return None


    def list_movies(self):
        movies = self.movie_manager.read_all_data_as_class()
        if not movies:
            print("Фильмы не найдены")
            return []
        for m in movies:
            print(f"{m.id}. {m.title} {m.release_year} рейтинг {m.rating}")
        return movies

    def rate_movie(self, user_id: int, movie_id: int, rating: float):
        user = self.user_manager.get_class_for_index(str(user_id))
        if user is None:
            print("Пользователь не найден")
            return None

        user.movie_history_with_rating[str(movie_id)] = float(rating)
        self.user_manager.update(user)
        return user

    def get_recommendations(self, user_id: int):
        user = self.user_manager.get_class_for_index(str(user_id))
        if user is None:
            print("Пользователь не найден")
            return []

        rec = set()
        rec |= GenreRecommendationStrategy(user).get_recommendations()
        rec |= RatingRecommendationStrategy(user).get_recommendations()
        rec |= SimilarUsersRecommendationStrategy(user).get_recommendations()

        movies = []
        for mid in rec:
            m = self.movie_manager.get_class_for_index(str(mid))
            if m:
                movies.append(m)
        return movies

    def filter_by_rating(self, min_rating=0, max_rating=10):
        movies = self.movie_manager.read_all_data_as_class()
        return [m for m in movies if min_rating <= m.rating <= max_rating]

    def filter_by_year(self, start_year=None, end_year=None):
        movies = self.movie_manager.read_all_data_as_class()
        if start_year is None: start_year = 0
        if end_year is None: end_year = 9999
        return [m for m in movies if start_year <= m.release_year <= end_year]