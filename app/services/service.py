from app.data_manager.manager import User_Manager, Movie_Manager, Genre_Manager
from app.models.user import User
from app.recomendations.be_genre import GenreRecommendationStrategy 
from app.recomendations.by_rating import RatingRecommendationStrategy
from app.recomendations.by_similar_users import SimilarUsersRecommendationStrategy


class UserService:
    def __init__(self):
        self.user_manager = User_Manager()
        self.movie_manager = Movie_Manager()
        self.genre_manager = Genre_Manager()

    def register_user(self, nickname: str):
        return self.user_manager.add(nickname)

    def login_user(self, user_id: int):
        try:
            return self.user_manager.get_class_for_index(str(user_id))
        except KeyError:
            print("Пользователь не найден")
            return None

    def delete_user(self, user_id: int):
        try:
            self.user_manager.remove(user_id)
        except KeyError:
            print("Пользователь не существует")
    def list_genres(self):
        genres = self.genre_manager.read_all_data_as_class()
        if not genres:
            print("Жанры не найдены")
            return []
        print("\nСписок доступных жанров (ID. Название):")
        for g in genres:
            print(f"{g.id}. {g.name}")
        return genres

    def set_preferred_genres(self, user_id: int, genre_ids: list):
        try:
            user = self.user_manager.get_class_for_index(str(user_id))
        except KeyError:
            print("Пользователь не найден")
            return None
        
        valid_genre_ids = []
        for g_id in genre_ids:
            try:
                self.genre_manager.get_class_for_index(str(g_id))
                valid_genre_ids.append(g_id)
            except KeyError:
                print(f"Жанр с ID {g_id} не найден. Пропускаем.")
                continue

        user.add_preferred_genres(valid_genre_ids)
        self.user_manager.update(user)
        print(f"Предпочтения для {user.nickname} обновлены")
        print(f"Текущие предпочтения (ID): {user.preferred_genres}")
        return user


    def list_movies(self):
        movies = self.movie_manager.read_all_data_as_class()
        if not movies:
            print("Фильмы не найдены")
            return []
        print("\nФильмы (ID. Название (Год) — Рейтинг/10):")
        for m in movies:
            print(f"{m.id}. {m.title} {m.release_year} рейтинг {m.rating}")
        return movies

    def rate_movie(self, user_id: int, movie_id: int, rating: float):
        user = self.user_manager.get_class_for_index(str(user_id))
        if user is None:
            print("Пользователь не найден")
            return None

        try:
            movie = self.movie_manager.get_class_for_index(str(movie_id))
            movie.add_rating(rating)
            self.movie_manager.update(movie)
        except KeyError:
            print("Фильм не найден")
            return None
            
        user.add_movie_history(movie_id, rating)
        self.user_manager.update(user)
        return user

    def get_recommendations(self, user_id: int):
        user = self.user_manager.get_class_for_index(str(user_id))
        
        if user is None:
            print("Пользователь не найден")
            return []

        rec = set()
        if user.preferred_genres:
            rec |= GenreRecommendationStrategy(user).get_recommendations()
            
        rec |= RatingRecommendationStrategy(user).get_recommendations()
        rec |= SimilarUsersRecommendationStrategy(user).get_recommendations()

        movies = []
        for mid in rec:
            try:
                movies.append(self.movie_manager.get_class_for_index(str(mid)))
            except KeyError:
                pass
                
        return movies


    def get_recommendations_by_genre(self, user_id: int):
        user = self.user_manager.get_class_for_index(str(user_id))

        if user is None:
            print("Пользователь не найден")
            return []

        if not user.preferred_genres:
            print("У пользователя нет предпочтительных жанров")
            return []

        rec = GenreRecommendationStrategy(user).get_recommendations()

        movies = []
        for mid in rec:
            try:
                movies.append(self.movie_manager.get_class_for_index(str(mid)))
            except KeyError:
                pass

        return movies


    def get_recommendations_by_rating(self, user_id: int):
        user = self.user_manager.get_class_for_index(str(user_id))

        if user is None:
            print("Пользователь не найден")
            return []

        rec = RatingRecommendationStrategy(user).get_recommendations()

        movies = []
        for mid in rec:
            try:
                movies.append(self.movie_manager.get_class_for_index(str(mid)))
            except KeyError:
                pass

        return movies


    def get_recommendations_by_similar_users(self, user_id: int):
        user = self.user_manager.get_class_for_index(str(user_id))

        if user is None:
            print("Пользователь не найден")
            return []

        rec = SimilarUsersRecommendationStrategy(user).get_recommendations()

        movies = []
        for mid in rec:
            try:
                movies.append(self.movie_manager.get_class_for_index(str(mid)))
            except KeyError:
                pass

        return movies

    def filter_recommendations(self, movies: list, min_rating: int =None, min_year: int = None, max_year: int = None) -> list:
        """
        Фильтрует фильмы по минимальному рейтингу и диапазону года выпуска.

        Args:
            movies (list из классов): список рекомендованных фильмов.
            min_rating (float | None): минимальный допустимый рейтинг.
            min_year (int | None): нижняя граница года выпуска.
            max_year (int | None): верхняя граница года выпуска.

        Returns:
            List[Movie]: список фильмов, прошедших фильтрацию.
        """
        filtered = []

        for movie in movies:
            # фильтр рейтинга
            if min_rating is not None and movie.rating < min_rating:
                continue

            # фильтр диапазона года выпуска
            if min_year is not None and movie.release_year < min_year:
                continue

            if max_year is not None and movie.release_year > max_year:
                continue

            filtered.append(movie)

        return filtered

