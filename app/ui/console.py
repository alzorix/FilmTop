from app.services.service import UserService

service = UserService()

def run_console():
    print(r"""
███████╗██╗██╗░░░░░███╗░░░███╗████████╗░█████╗░██████╗░   1. Регистрация
██╔════╝██║██║░░░░░████╗░████║╚══██╔══╝██╔══██╗██╔══██╗   2. Вход
█████╗░░██║██║░░░░░██╔████╔██║░░░██║░░░██║░░██║██████╔╝   3. Список фильмов
██╔══╝░░██║██║░░░░░██║╚██╔╝██║░░░██║░░░██║░░██║██╔═══╝░   4. Оценить фильм
██║░░░░░██║███████╗██║░╚═╝░██║░░░██║░░░╚█████╔╝██║░░░░░   5. Рекомендации
╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░░░░   0. Выход
""")

    user = None

    while 1:
        choice = input("Выберите действие: ")

        if choice == "1":
            nickname = input("Введите имя: ")
            user = service.register_user(nickname)
            print(f"Зарегистрирован пользователь: {user.nickname} (ID: {user.id})")
        elif choice == "2":
            uid = input("Введите ID пользователя: ")
            user = service.login_user(int(uid))
            if user:
                print(f"Вошёл пользователь: {user.nickname}")
        elif choice == "3":
            service.list_movies()
        elif choice == "4":
            if not user:
                print("Сначала войдите в систему")
                continue
            movie_id = int(input("ID фильма: "))
            rating = float(input("Ваша оценка: "))
            service.rate_movie(user.id, movie_id, rating)
            print("Оценка сохранена")
        elif choice == "5":
            if not user:
                print("Сначала войдите в систему")
                continue
            recs = service.get_recommendations(user.id)
            if recs:
                print("Рекомендованные фильмы:")
                for m in recs:
                    print(f"{m.id}. {m.title} ({m.release_year}) - {m.rating}/10")
            else:
                print("Нет рекомендаций")
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор")