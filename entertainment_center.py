import media
import fresh_tomatoes

toy_story = media.Movie("Title", "Storyline",
 "http://cdn.collider.com/wp-content/uploads/my-neighbor-totoro-poster-variant-olly-moss-mondo.jpg", "https://www.youtube.com/watch?v=92a7Hj0ijLs")


movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)
