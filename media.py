import webbrowser


class Movie():

    def __init__(self, movie_title, movie_story, pos_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = pos_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
