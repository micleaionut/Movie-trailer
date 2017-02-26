# import module
import webbrowser


# create class Movie
class Movie():
    def __init__(self, movie_title, movie_story, poster_img, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube
