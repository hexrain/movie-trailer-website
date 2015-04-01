from movie import Movie


def all_movies():
    """Generates movie list

    Returns:
        Array of Movie objects
    """
    return [
        Movie(title="Matrix",
              trailer="https://youtu.be/m8e-FF8MsqU",
              poster_url="http://st-im.kinopoisk.ru/im/poster/7/3/3/kinopoisk.ru-The-Matrix-733005.jpg",
              imdb_url="http://www.imdb.com/title/tt0133093"),

        Movie(title="Avatar",
              trailer="https://www.youtu.be/cRdxXPV9GNQ",
              poster_url="http://www.impawards.com/2009/posters/avatar_xlg.jpg",
              imdb_url="http://www.imdb.com/title/tt0499549"),

        Movie(title="Spider-Man",
              trailer="https://www.youtu.be/FN3YaybNJ2s",
              poster_url="http://cdn.screenrant.com/wp-content/uploads/Original-Spider-Man-Movie-Poster.jpg",
              imdb_url="http://www.imdb.com/title/tt0145487"),
    ]
