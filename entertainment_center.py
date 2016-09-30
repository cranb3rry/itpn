import media
import fresh_tomatoes

# Title, storyline, poster URL, trailer URL inputs for Movie

my_neighbor_totoro = media.Movie(
	"My Neighbor Totoro",
	"Storyline",
	"https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
	"https://www.youtube.com/watch?v=92a7Hj0ijLs"
  )

star_wars_v = media.Movie(
	"Star Wars: Episode V",
	"Storyline",
	"https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
	"https://www.youtube.com/watch?v=mz_YWNhKOkM"
  )

lotr_rk = media.Movie(
	"The Lord of the Rings: The Return of the King",
	"Storyline",
	"https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
	"https://www.youtube.com/watch?v=r5X-hFf6Bwo"
  )

# Movie instances


movies = [my_neighbor_totoro, star_wars_v, lotr_rk]

fresh_tomatoes.open_movies_page(movies)
