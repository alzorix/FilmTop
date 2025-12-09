genres = [
    "Боевик", "Приключения", "Комедия", "Драма", "Триллер",
    "Ужасы", "Фантастика", "Фэнтези", "Мелодрама", "Детектив",
    "Криминал", "Исторический", "Военный", "Музыкальный", "Мюзикл",
    "Анимация", "Документальный", "Спортивный", "Семейный", "Биографический",
    "Романтический", "Сюрреализм", "Мистика", "Психологический", "Постапокалипсис"
]
import manager

genre_manager = manager.Genre_Manager()

# for genre_name in genres:
#     added_genre = genre_manager.add(genre_name)
#     print(f"Добавлен жанр: {added_genre.id} - {added_genre.name}")
#



movie_manager = manager.Movie_Manager()




movies_list = [
    {
        "title": "Бегемот в тапочках",
        "genres_id": [3, 19],
        "director": "Василий Шуткин",
        "release_year": 2022,
        "rating": 7.4,
        "rating_count": 1583
    },
    {
        "title": "Тарелка на Луне",
        "genres_id": [7, 8, 22],
        "director": "Марфа Луновская",
        "release_year": 2025,
        "rating": 8.1,
        "rating_count": 924
    },
    {
        "title": "Дядя Фёдор против холодильника",
        "genres_id": [1, 2, 3],
        "director": "Игорь Блинчик",
        "release_year": 2019,
        "rating": 6.9,
        "rating_count": 2041
    },
    {
        "title": "Танцы с кактусами",
        "genres_id": [15, 14, 3],
        "director": "Екатерина Пирожкова",
        "release_year": 2021,
        "rating": 7.8,
        "rating_count": 1187
    },
    {
        "title": "Пёс на крыше",
        "genres_id": [19, 3, 9],
        "director": "Виталий Шариков",
        "release_year": 2020,
        "rating": 8.3,
        "rating_count": 872
    },
    {
        "title": "Кот против машины времени",
        "genres_id": [7, 8, 1],
        "director": "София Мурлыкаева",
        "release_year": 2024,
        "rating": 9.0,
        "rating_count": 1432
    },
    {
        "title": "Огурцы атакуют",
        "genres_id": [1, 5, 3],
        "director": "Дмитрий Хрустальный",
        "release_year": 2023,
        "rating": 6.5,
        "rating_count": 1125
    },
    {
        "title": "Секретный дневник йети",
        "genres_id": [8, 22, 23],
        "director": "Александра Лаптёшкина",
        "release_year": 2026,
        "rating": 8.7,
        "rating_count": 667
    },
    {
        "title": "Торт против вселенной",
        "genres_id": [3, 7, 25],
        "director": "Павел Булкин",
        "release_year": 2027,
        "rating": 7.9,
        "rating_count": 421
    },
    {
        "title": "Кролики и правительство",
        "genres_id": [11, 1, 3],
        "director": "Ольга Шлёпкина",
        "release_year": 2021,
        "rating": 6.8,
        "rating_count": 1345
    },
    {
        "title": "Бегемот в тапочках",
        "genres_id": [3, 19],
        "director": "Василий Шуткин",
        "release_year": 2022,
        "rating": 7.4,
        "rating_count": 1583
    },
    {
        "title": "Тарелка на Луне",
        "genres_id": [7, 8, 22],
        "director": "Марфа Луновская",
        "release_year": 2025,
        "rating": 8.1,
        "rating_count": 924
    },
    {
        "title": "Дядя Фёдор против холодильника",
        "genres_id": [1, 2, 3],
        "director": "Игорь Блинчик",
        "release_year": 2019,
        "rating": 6.9,
        "rating_count": 2041
    },
    {
        "title": "Танцы с кактусами",
        "genres_id": [15, 14, 3],
        "director": "Екатерина Пирожкова",
        "release_year": 2021,
        "rating": 7.8,
        "rating_count": 1187
    },
    {
        "title": "Пёс на крыше",
        "genres_id": [19, 3, 9],
        "director": "Виталий Шариков",
        "release_year": 2020,
        "rating": 8.3,
        "rating_count": 872
    },
    {
        "title": "Кот против машины времени",
        "genres_id": [7, 8, 1],
        "director": "София Мурлыкаева",
        "release_year": 2024,
        "rating": 9.0,
        "rating_count": 1432
    },
    {
        "title": "Огурцы атакуют",
        "genres_id": [1, 5, 3],
        "director": "Дмитрий Хрустальный",
        "release_year": 2023,
        "rating": 6.5,
        "rating_count": 1125
    },
    {
        "title": "Секретный дневник йети",
        "genres_id": [8, 22, 23],
        "director": "Александра Лаптёшкина",
        "release_year": 2026,
        "rating": 8.7,
        "rating_count": 667
    },
    {
        "title": "Торт против вселенной",
        "genres_id": [3, 7, 25],
        "director": "Павел Булкин",
        "release_year": 2027,
        "rating": 7.9,
        "rating_count": 421
    },
    {
        "title": "Кролики и правительство",
        "genres_id": [11, 1, 3],
        "director": "Ольга Шлёпкина",
        "release_year": 2021,
        "rating": 6.8,
        "rating_count": 1345
    },
    {
        "title": "Велосипед против динозавра",
        "genres_id": [2, 1, 7],
        "director": "Григорий Пружинкин",
        "release_year": 2030,
        "rating": 7.2,
        "rating_count": 998
    },
    {
        "title": "Мороженое на Марсе",
        "genres_id": [7, 8, 3],
        "director": "Надежда Сливкина",
        "release_year": 2028,
        "rating": 8.5,
        "rating_count": 730
    },
    {
        "title": "Слон в музыкальной шляпе",
        "genres_id": [14, 3, 15],
        "director": "Валерий Трусов",
        "release_year": 2018,
        "rating": 6.7,
        "rating_count": 1102
    },
    {
        "title": "Пиратский понедельник",
        "genres_id": [2, 1, 3],
        "director": "Людмила Капустина",
        "release_year": 2017,
        "rating": 7.6,
        "rating_count": 1401
    },
    {
        "title": "Танцующие кактусы 2",
        "genres_id": [15, 14, 3],
        "director": "Екатерина Пирожкова",
        "release_year": 2023,
        "rating": 7.9,
        "rating_count": 923
    },
    {
        "title": "Бананы в космосе",
        "genres_id": [7, 8, 3],
        "director": "Семен Обезьянов",
        "release_year": 2025,
        "rating": 8.2,
        "rating_count": 555
    },
    {
        "title": "Мыши и ковбои",
        "genres_id": [2, 1, 3],
        "director": "Алексей Сыров",
        "release_year": 2019,
        "rating": 6.9,
        "rating_count": 1340
    },
    {
        "title": "Доктор Пельмень",
        "genres_id": [3, 4, 9],
        "director": "Ирина Вареникина",
        "release_year": 2021,
        "rating": 7.5,
        "rating_count": 874
    },
    {
        "title": "Кот в сапогах против принтера",
        "genres_id": [1, 3, 7],
        "director": "Михаил Лапкин",
        "release_year": 2024,
        "rating": 8.0,
        "rating_count": 642
    },
    {
        "title": "Сырные войны",
        "genres_id": [1, 2, 3],
        "director": "Анастасия Сырникова",
        "release_year": 2022,
        "rating": 7.3,
        "rating_count": 987
    },
    {
        "title": "Панда против тостера",
        "genres_id": [1, 3, 7],
        "director": "Виктория Пушистая",
        "release_year": 2023,
        "rating": 7.1,
        "rating_count": 821
    },
    {
        "title": "Робот-бариста",
        "genres_id": [7, 3, 14],
        "director": "Никита Эспрессов",
        "release_year": 2025,
        "rating": 8.4,
        "rating_count": 610
    },
    {
        "title": "Гигантский хот-дог",
        "genres_id": [3, 19],
        "director": "Олег Сосискин",
        "release_year": 2021,
        "rating": 6.9,
        "rating_count": 940
    },
    {
        "title": "Кролики на Луне",
        "genres_id": [8, 2, 3],
        "director": "Мария Морковкина",
        "release_year": 2024,
        "rating": 8.2,
        "rating_count": 523
    },
    {
        "title": "Супер-пельмени",
        "genres_id": [1, 3, 21],
        "director": "Георгий Лапшов",
        "release_year": 2022,
        "rating": 7.5,
        "rating_count": 711
    },
    {
        "title": "Викинги и блинчики",
        "genres_id": [2, 3, 12],
        "director": "Ольга Блинкина",
        "release_year": 2020,
        "rating": 7.8,
        "rating_count": 804
    },
    {
        "title": "Пельмень в космосе",
        "genres_id": [7, 8, 3],
        "director": "Игорь Вареников",
        "release_year": 2026,
        "rating": 8.6,
        "rating_count": 412
    },
    {
        "title": "Слон на скейтборде",
        "genres_id": [1, 3, 18],
        "director": "Леонид Трамвайкин",
        "release_year": 2019,
        "rating": 7.2,
        "rating_count": 679
    },
    {
        "title": "Кот против холодильника 2",
        "genres_id": [1, 3, 7],
        "director": "София Мурлыкаева",
        "release_year": 2028,
        "rating": 8.1,
        "rating_count": 515
    },
    {
        "title": "Мыши и шоколад",
        "genres_id": [3, 19],
        "director": "Алексей Сыров",
        "release_year": 2023,
        "rating": 7.4,
        "rating_count": 642
    },
    {
        "title": "Доктор Морковкин",
        "genres_id": [3, 4, 9],
        "director": "Ирина Вареникина",
        "release_year": 2022,
        "rating": 7.6,
        "rating_count": 578
    },
    {
        "title": "Пингвины на пляже",
        "genres_id": [3, 19, 2],
        "director": "Валентина Лёдова",
        "release_year": 2025,
        "rating": 8.0,
        "rating_count": 433
    },
    {
        "title": "Торт и пришельцы",
        "genres_id": [3, 7, 25],
        "director": "Павел Булкин",
        "release_year": 2027,
        "rating": 7.9,
        "rating_count": 421
    },
    {
        "title": "Кролики и драконы",
        "genres_id": [8, 2, 3],
        "director": "Анастасия Зайцева",
        "release_year": 2024,
        "rating": 8.3,
        "rating_count": 376
    },
    {
        "title": "Гигантская морковка",
        "genres_id": [3, 2, 19],
        "director": "Семен Овощкин",
        "release_year": 2021,
        "rating": 7.0,
        "rating_count": 512
    },
    {
        "title": "Йети на вечеринке",
        "genres_id": [8, 3, 22],
        "director": "Александра Лаптёшкина",
        "release_year": 2026,
        "rating": 8.7,
        "rating_count": 667
    },
    {
        "title": "Пельмени против зомби",
        "genres_id": [1, 6, 3],
        "director": "Игорь Хрустальный",
        "release_year": 2023,
        "rating": 6.8,
        "rating_count": 431
    },
    {
        "title": "Сырная империя",
        "genres_id": [1, 3, 11],
        "director": "Анастасия Сырникова",
        "release_year": 2022,
        "rating": 7.3,
        "rating_count": 514
    },
    {
        "title": "Танцующие слоны",
        "genres_id": [3, 15],
        "director": "Екатерина Пирожкова",
        "release_year": 2023,
        "rating": 7.8,
        "rating_count": 492
    },
    {
        "title": "Кот в шляпе и холодильник",
        "genres_id": [1, 3, 7],
        "director": "Михаил Лапкин",
        "release_year": 2024,
        "rating": 8.0,
        "rating_count": 642
    },
    {
        "title": "Бананы на луне",
        "genres_id": [7, 8, 3],
        "director": "Семен Обезьянов",
        "release_year": 2025,
        "rating": 8.2,
        "rating_count": 555
    },
    {
        "title": "Робот и морковь",
        "genres_id": [7, 3, 14],
        "director": "Никита Эспрессов",
        "release_year": 2025,
        "rating": 8.4,
        "rating_count": 610
    },
    {
        "title": "Слон и тостер",
        "genres_id": [1, 3, 7],
        "director": "Виктория Пушистая",
        "release_year": 2023,
        "rating": 7.1,
        "rating_count": 821
    },
    {
        "title": "Мыши и пельмени",
        "genres_id": [3, 19],
        "director": "Алексей Сыров",
        "release_year": 2023,
        "rating": 7.4,
        "rating_count": 642
    },
    {
        "title": "Доктор Холодильников",
        "genres_id": [3, 4, 9],
        "director": "Ирина Вареникина",
        "release_year": 2022,
        "rating": 7.6,
        "rating_count": 578
    },
    {
        "title": "Пингвины против пиццы",
        "genres_id": [3, 19, 2],
        "director": "Валентина Лёдова",
        "release_year": 2025,
        "rating": 8.0,
        "rating_count": 433
    },
    {
        "title": "Кролики и морковь",
        "genres_id": [8, 2, 3],
        "director": "Анастасия Зайцева",
        "release_year": 2024,
        "rating": 8.3,
        "rating_count": 376
    },
    {
        "title": "Гигантские блинчики",
        "genres_id": [3, 2, 19],
        "director": "Семен Овощкин",
        "release_year": 2021,
        "rating": 7.0,
        "rating_count": 512
    },
    {
        "title": "Йети и пельмени",
        "genres_id": [8, 3, 22],
        "director": "Александра Лаптёшкина",
        "release_year": 2026,
        "rating": 8.7,
        "rating_count": 667
    }
]



for movie in movies_list:
    movie_manager.add(
        movie_name=movie["title"],
        genres_id=movie["genres_id"],
        director=movie["director"],
        release_year=movie["release_year"],
        raiting=movie.get("rating"),
        rating_count=movie.get("rating_count")
    )
    print("Вроде ЗБС")