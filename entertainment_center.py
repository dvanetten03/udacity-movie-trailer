import fresh_tomatoes

import media

# movie title, storyline, poster image and movie trailer
american_sniper = media.Movie(
    "American Sniper",
     "True story of a true American hero, Chris Kyle",
     "http://t2.gstatic.com/images?q=tbn:ANd9GcSCEJMtX2_SB-ZlvYpabgPb6dwI_bVSY-eVap6aSSSfFq5Ldmxa",  # NOQA
     "https://www.youtube.com/watch?v=99k3u9ay1gs")

# movie title, storyline, poster image and movie trailer
mission_impossible = media.Movie(
    "Mission Impossible",
    "Ethan Hunt needs to prove his innocence and keep the world safe",
    "https://upload.wikimedia.org/wikipedia/en/e/e1/MissionImpossiblePoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=gOW_azQbOjw")

# movie title, storyline, poster image and movie trailer
wonder_woman = media.Movie(
    "Wonder Woman",
    "Diana Prince comes out from the shadows to save the world",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H",  # NOQA
    "https://www.youtube.com/watch?v=VSB4wGIdDwo")

# movie title, storyline, poster image and movie trailer
the_hobbit = media.Movie(
    "The Hobbit",
    "A reluctant hobbit, Bilbo Baggins, sets out on a journey with a"
    "spirited group of dwarves to reclaim their home",
    "http://cdn.collider.com/wp-content/uploads/hobbit-unexpected-journey-imax-poster-andy-serkis.jpg",  # NOQA
    "https://www.youtube.com/watch?v=nOGsB9dORBg")

# movie title, storyline, poster image and movie trailer
the_avengers = media.Movie(
    "The Avengers",
    "Earth's mightiest heroes need to work together to save the world",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# movie: movie title, storyline, poster image and movie trailer
zero_dark_thirty = media.Movie(
    "Zero Dark Thirty",
    "The Greatest Manhunt in History",
    "http://static.metacritic.com/images/products/movies/8/a22d5b5f78fbbea4f6f8f19b6dbd00e5.jpg",   # NOQA
    "www.youtube.com/watch?v=mejkiIvnkzY")

# set the movies to be passed to the media file
movies = [
    american_sniper,
    mission_impossible,
    wonder_woman,
    the_hobbit,
    the_avengers,
    zero_dark_thirty
]

# open the HTML file in a web browser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
