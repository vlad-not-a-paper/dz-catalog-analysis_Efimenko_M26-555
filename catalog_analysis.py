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
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

index = 0
while index < len(movies):
    if movies[index]["rating"] > 9:
        print(movies[index]["title"])
        break
    index += 1
else:
    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    title_list = []
    for word in title.split():
        title_list.append(word[0].upper() + word[1:])
    normalized_title = " ".join(title_list)
    return normalized_title


def make_slug(title):
    slug_list = []
    for word in title.split():
        slug_list.append(word.lower())
    slugged_title = "-".join(slug_list)
    return slugged_title


def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    report_line = f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'
    return report_line


def titles_sorted_by_rating(movies):
    ratings = []
    rating_title = dict()
    sorted_titles = []
    for movie in movies:
        ratings.append(movie["rating"])
        rating_title[movie["rating"]] = movie["title"]
    ratings.sort(reverse=True)
    for rating in ratings:
        sorted_titles.append(rating_title[rating])
    return sorted_titles


def top_n_by_rating(movies, n=3):
    top = []
    ratings = []
    rating_title = dict()
    for movie in movies:
        ratings.append(movie["rating"])
        rating_title[movie["rating"]] = movie["title"]
    ratings.sort(reverse=True)
    for i in range(n):
        top.append((rating_title[ratings[i]], ratings[i]))
    return top


def count_by_genre(movies):
    genres = dict()
    for movie in movies:
        for genre in movie["genres"]:
            genres[genre] = genres.get(genre, 0) + 1
    return genres


def actor_filmography(movies):
    actors = dict()
    for movie in movies:
        for actor in movie["actors"]:
            if actors.get(actor, 0) == 0:
                actors[actor] = [movie["title"]]
            else:
                actors[actor].append(movie["title"])
    return actors


avg_rating = average_rating(movies)
film_score = {
    movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avg_rating
}


def all_genres(movies):
    genres_set = set()
    for movie in movies:
        genres_set.update(movie["genres"])
    return genres_set


def common_actors(movie1, movie2):
    actors1 = set()
    actors2 = set()
    actors1.update(movie1["actors"])
    actors2.update(movie2["actors"])
    return actors1 & actors2


def genres_only_in_one(movies_a, movies_b):
    genre_a = set()
    genre_b = set()
    for movie in movies_a:
        genre_a.update(movie["genres"])
    for movie in movies_b:
        genre_b.update(movie["genres"])
    return genre_a - genre_b


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


for movie in iter_high_rated(movies):
    print(format_report_line(movie))

sum(m['duration_min'] for m in movies if m['rating'] > 7)


def build_report(movies):
    report = ["ОТЧеТ ПО КАТАЛОГУ"]
    report.append(f"Средний рейтинг: {average_rating(movies)}")
    report.append(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")
    report.append("")
    report.append("Топ-3 фильма:")
    top = top_n_by_rating(movies)
    for film in top:
        for movie in movies:
            if movie["title"] == film[0]:
                report.append(format_report_line(movie))
    report.append("")
    report.append("Фильмов по жанрам:")
    genres_count = count_by_genre(movies)
    sorted_genres_count = []
    for genre in genres_count:
        sorted_genres_count.append(
            f"{genres_count[genre]}  {genre} — {genres_count[genre]}"
        )
    sorted_genres_count.sort(reverse=True)
    for string in sorted_genres_count:
        report.append(string[1:])
    report.append("")
    report.append(f"Все жанры каталога: {', '.join(sorted(all_genres(movies)))}")
    return "\n".join(report)


if __name__ == "__main__":
    print(build_report(movies))