# import modules
import fresh_tomatoes
import media
# send paramaters to Movie class and save it
gamer = media.Movie("Gamer",
                    "In a future mind-controlling game, death row convicts"
                    "are forced to battle in a Doom-type environment."
                    "Convict Kable, controlled by Simon, a skilled teenage"
                    "gamer",
                    "https://s-media-cache-ak0.pinimg.com/originals/85/"
                    "a6/3d/85a63dee6e9accb112f1cfccd5dfbd86.jpg",
                    "https://www.youtube.com/watch?v=ECoPbiGfjNw")
# send paramaters to Movie class and save it
jaws = media.Movie("Jaws",
                   "Jaws is an American natural horror film series that"
                   "started with a 1975 film that expanded into three"
                   "sequels, a theme park ride",
                   "http://i.ebayimg.com/00/s/MTYwMFgxMDY2/z/"
                   "0a8AAOSwBahVDB2H/$_32.JPG",
                   "https://www.youtube.com/watch?v=U1fu_sA7XhE")
# send paramaters to Movie class and save it
atm = media.Movie("ATM - Trappola mortale",
                  "ATM - Trappola mortale (ATM) e un film del 2012 diretto"
                  "da David Brooks, interpretato da Alice Eve, Josh Peck "
                  "e Brian Geraghty.",
                  "http://graphicdesignjunction.com/wp-content/uploads/2012/"
                  "03/movies-poster-26.jpg",
                  "https://www.youtube.com/watch?v=9ac-P1s95-4")
# send paramaters to Movie class and save it
theforest = media.Movie("The forest",
                        "A woman goes into Japans Suicide Forest to find her"
                        "twin sister, and confronts supernatural terror. ",
                        "http://graphicdesignjunction.com/wp-content/uploads/"
                        "2016/01/005-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=RBc5YcuOThY")
# send paramaters to Movie class and save it
disaster = media.Movie("Disaster",
                       "2012 is a 2009 American disaster film directed by "
                       "Roland Emmerich, and stars John Cusack, Chiwetel"
                       "Ejiofor, Amanda Peet,",
                       "https://designmodo.com/wp-content/uploads/2011/02/"
                       "Creative-Movie-Posters-71.jpg",
                       "https://www.youtube.com/watch?v=rvI66Xaj9-o")
# send paramaters to Movie class and save it
startrek = media.Movie("Star trek",
                       "The USS Enterprise crew explores the furthest reaches"
                       "of uncharted space, where they encounter a new"
                       " ruthless enemy.",
                       "http://www.printmag.com/wp-content/uploads/"
                       "star_trek_xi_ver16_xlg.jpg?91875e",
                       "https://www.youtube.com/watch?v=XRVD32rnzOw")
# add movies saved in array called movies
movies = [gamer, jaws, atm, theforest, disaster, startrek]
# send movies array to open_movies_page
fresh_tomatoes.open_movies_page(movies)
