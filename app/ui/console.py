from app.services.service import UserService
import re

service = UserService()

def run_console():
    print(r"""
███████╗██╗██╗░░░░░███╗░░░███╗████████╗░█████╗░██████╗░     1. Регистрация
██╔════╝██║██║░░░░░████╗░████║╚══██╔══╝██╔══██╗██╔══██╗     2. Вход
█████╗░░██║██║░░░░░██╔████╔██║░░░██║░░░██║░░██║██████╔╝     3. Список фильмов
██╔══╝░░██║██║░░░░░██║╚██╔╝██║░░░██║░░░██║░░██║██╔═══╝░     4. Оценить фильм
██║░░░░░██║███████╗██║░╚═╝░██║░░░██║░░░╚█████╔╝██║░░░░░     5. Рекомендации
╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░░░░     6. Настроить любимые жанры
                                                            0. Выход
""")

    user = None

    while True:
        choice = input(f"\nПользователь: {user.nickname if user else 'Нет'} | Выберите действие: ")

        if choice == "1":
            nickname = input("Введите имя: ")
            user = service.register_user(nickname)
            print(f"Зарегистрирован пользователь: {user.nickname} (ID: {user.id})")
        
        elif choice == "2":
            try:
                uid = int(input("Введите ID пользователя: "))
                user = service.login_user(uid)
                if user:
                    print(f"Вошел пользователь: {user.nickname}")
            except ValueError:
                print("ID должен быть числом.")

        elif choice == "3":
            service.list_movies()
        
        elif choice in ("4", "5", "6") and user is None:
            print("Сначала войдите в систему (2)")
            
        elif choice == "4":
            try:
                movie_id = int(input("ID фильма для оценки: "))
                rating = float(input("Ваша оценка (0.0-10.0): "))
                if 0.0 <= rating <= 10.0:
                    service.rate_movie(user.id, movie_id, rating)
                    print("Оценка сохранена.")
                else:
                    print("Рейтинг должен быть от 0.0 до 10.0.")
            except ValueError:
                print("ID фильма и оценка должны быть числами.")
            except KeyError as e:
                print(f"Ошибка: {e}")

        elif choice == "5":
            recs = service.get_recommendations(user.id)
            
            if recs:
                print("\nРекомендованные фильмы:")
                for m in recs:
                    print(f"({m.rating}/10) {m.id}. {m.title} ({m.release_year})")
            else:
                print("Нет рекомендаций. Попробуйте оценить больше фильмов и настроить жанры.")
        
        elif choice == "6":
            genres = service.list_genres()
            if not genres:
                continue 
            genre_input = input("Введите ID любимых жанров через запятую: ")
            
            try:
                genre_ids = [int(g.strip()) for g in re.findall(r'\d+', genre_input)]
                
                if genre_ids:
                    service.set_preferred_genres(user.id, genre_ids)
                else:
                    print("Никакие ID жанров не были введены")
                    
            except ValueError:
                print("Ошибка ввода")

        elif choice == "0":
            print("Выход...")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")