#Creating Parent class Video
class Video():
    def __init__(self, video_Title, video_Storyline, poster_Image, trailer_Youtube_Url):
        self.title = video_Title
        self.storyline = video_Storyline
        self.trailer_youtube_url = trailer_Youtube_Url
        self.poster_image_url = poster_Image

#Creating child class Movie, with parent class Video
class Movie(Video):
    def __init__(self, video_Title, video_Storyline, poster_Image, trailer_Youtube_Url, movie_Rating):
        Video.__init__(self, video_Title, video_Storyline, poster_Image, trailer_Youtube_Url)
        self.rating = movie_Rating

#Creating child class Tv_Show, with parent class Video
class Tv_Show(Video):
    def __init__(self, video_Title, video_Storyline,poster_Image, trailer_Youtube_Url, number_Seasons):
        Video.__init__(self, video_Title, video_Storyline, poster_Image, trailer_Youtube_Url)
        self.seasons = number_Seasons
