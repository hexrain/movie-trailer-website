import fresh_tomatoes
import database
from movie import Movie

# Load movies from database. I used this approach to encapsulate data
# access logic
movies = database.all_movies()

# We should open our website in user's browser

fresh_tomatoes.open_movies_page(movies)
