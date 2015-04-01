class Movie(object):

    """Represents a movie

    Attributes:
        trailer_youtube_url: A string url of a youtube trailer.
        title: A string containing the title of a movie.
        poster_image_url: A string url pointing to a poster image.
        imdb_url: A string url pointing to the movie's imdb page
    """

    trailer_youtube_url = ""

    title = ""

    poster_image_url = ""

    imdb_url = ""

    def __init__(self, title, trailer, poster_url, imdb_url):
        """Inits Movie with title, trailer url, poster url and imdb_url"""
        super(Movie, self).__init__()
        self.title = title
        self.trailer_youtube_url = trailer
        self.poster_image_url = poster_url
        self.imdb_url = imdb_url
