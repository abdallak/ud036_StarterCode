class Movie():
    """ this Class encapsulat the properties of a movie in a movie object"""
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
