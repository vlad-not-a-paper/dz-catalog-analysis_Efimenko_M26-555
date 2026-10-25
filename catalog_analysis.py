import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    count = 0
    rating = 0
    for movie in movies:
        rating += movie["rating"]
        count += 1
    avg_rating = round(rating / count, 1)
    return avg_rating


def catalog_age_stats(movies, current_year=2026):
    count = 0
    years = 0
    oldest_film = -10_000
    newest_film = 10_000
    for movie in movies:
        count += 1
        age = current_year - movie["year"]
        years += age
        if oldest_film < age:
            oldest_film = age
        if newest_film > age:
            newest_film = age
    avg_year = math.ceil(years / count)
    return (oldest_film, newest_film, avg_year)


def duration_in_hours(minutes):
    recording_format = f"{minutes // 60}ч {minutes % 60}м"
    return recording_format


def rating_tier(rating):
    if rating >= 9:
        category = "шедевр"
    elif rating >= 7:
        category = "хорошо"
    else:
        category = "средне" if rating >= 5 else "слабо"
    return category


def decade_label(year):
    match year:
        case _ if year > 2020:
            mark = "новые"
        case _ if year >= 2015:
            mark = "недавние"
        case _:
            mark = "старые"
    return mark


for movie in movies:
    if "comedy" in movie['genres']:
        continue
    print(movie['title'])

index = 0
while index < len(movies):
    if movies[index]['rating'] > 9:
        print(movies[index]['title'])
        break
    index += 1
else:
    print('Шедевров не найдено')


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count