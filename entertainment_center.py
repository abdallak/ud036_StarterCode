import fresh_tomatoes
import media

mad_max = media.Movie("MAD MAX", "https://images-na.ssl-images-amazon.com/images/M/MV5BYTY2MTlhMTItZGFiOS00ZGM5LTlhYjUtZWU4NmZmOWJmNzc0XkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SY1000_CR0,0,666,1000_AL_.jpg", "https://www.youtube.com/watch?v=hEJnMQG9ev8")
inception = media.Movie ("INCEPTION" ,"https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg","https://www.youtube.com/watch?v=d3A3-zSOBT4")
bad_moms = media.Movie ("BAD MOMS", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIwNzE5MTgwNl5BMl5BanBnXkFtZTgwNjM4OTA0OTE@._V1_SY1000_CR0,0,675,1000_AL_.jpg","https://www.youtube.com/watch?v=jN7AYD6TqBQ")
black_panther = media.Movie ("BLACK PANTHER","https://images-na.ssl-images-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg","https://www.youtube.com/watch?v=xjDjIWPwcPU")
TMR = media.Movie ("THE MAZE RUNNER","https://images-na.ssl-images-amazon.com/images/M/MV5BMjUyNTA3MTAyM15BMl5BanBnXkFtZTgwOTEyMTkyMjE@._V1_.jpg","https://www.youtube.com/watch?v=64-iSYVmMVY")
memento = media.Movie("MEMENTO","https://images-na.ssl-images-amazon.com/images/M/MV5BZTcyNjk1MjgtOWI3Mi00YzQwLWI5MTktMzY4ZmI2NDAyNzYzXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,681,1000_AL_.jpg","https://www.youtube.com/watch?v=0vS0E9bBSL0")

movies= [mad_max,inception,black_panther,bad_moms,TMR,memento]

fresh_tomatoes.open_movies_page(movies)

