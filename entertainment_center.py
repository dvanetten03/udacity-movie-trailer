import fresh_tomatoes
import media

american_sniper = media.Movie("American Sniper", "True story of a true American hero, Chris Kyle", 
                             "http://t2.gstatic.com/images?q=tbn:ANd9GcSCEJMtX2_SB-ZlvYpabgPb6dwI_bVSY-eVap6aSSSfFq5Ldmxa", 
                             "https://www.youtube.com/watch?v=99k3u9ay1gs")

mission_impossible = media.Movie("Mission Impossible", "Ethan Hunt needs to prove his innocense", 
                                "https://upload.wikimedia.org/wikipedia/en/e/e1/MissionImpossiblePoster.jpg",
                                 "https://www.youtube.com/watch?v=gOW_azQbOjw")

wonder_woman = media.Movie("Wonder Woman", "Female Super Hero Movie", 
                          "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H", 
                          "https://www.youtube.com/watch?v=VSB4wGIdDwo")

the_hobbit = media.Movie("The Hobbit", "Hobbit's journey from the Shire into danger",
                        "https://i.pinimg.com/736x/01/aa/51/01aa51decf00c3418b54bd828b919494.jpg",
                        "https://www.youtube.com/watch?v=nOGsB9dORBg")

the_avengers = media.Movie("The Avengers", "Earth's mightiest heroes need to work together to save the world", 
                          "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", 
                          "https://www.youtube.com/watch?v=eOrNdBpGMv8")

zero_dark_thirty = media.Movie("Zero Dark Thirty", "The Greatest Manhunt in History", 
                              "http://static.metacritic.com/images/products/movies/8/a22d5b5f78fbbea4f6f8f19b6dbd00e5.jpg", 
                              "www.youtube.com/watch?v=mejkiIvnkzY")

movies = [american_sniper, mission_impossible, wonder_woman, the_hobbit, 
         the_avengers, zero_dark_thirty]

fresh_tomatoes.open_movies_page(movies)