import fresh_tomatoes
import media

gamer = media.Movie("Gamer",
                        "In a future mind-controlling game, death row convicts are forced to battle in a Doom-type environment. Convict Kable, controlled by Simon, a skilled teenage gamer, must survive thirty sessions in order to be set free. Or wont he? ",
                        "https://s-media-cache-ak0.pinimg.com/originals/85/a6/3d/85a63dee6e9accb112f1cfccd5dfbd86.jpg",
                        "https://www.youtube.com/watch?v=ECoPbiGfjNw")

jaws = media.Movie("Jaws",
                        "Jaws is an American natural horror film series that started with a 1975 film that expanded into three sequels, a theme park ride, and other tie-in merchandise, based on a 1974 novel",
                        "http://i.ebayimg.com/00/s/MTYwMFgxMDY2/z/0a8AAOSwBahVDB2H/$_32.JPG",
                        "https://www.youtube.com/watch?v=U1fu_sA7XhE")


atm = media.Movie("ATM - Trappola mortale",
                        "ATM - Trappola mortale (ATM) e un film del 2012 diretto da David Brooks, interpretato da Alice Eve, Josh Peck e Brian Geraghty.",
                        "http://graphicdesignjunction.com/wp-content/uploads/2012/03/movies-poster-26.jpg",
                        "https://www.youtube.com/watch?v=9ac-P1s95-4")


theforest = media.Movie("The forest",
                        "A woman goes into Japans Suicide Forest to find her twin sister, and confronts supernatural terror. ",
                        "http://graphicdesignjunction.com/wp-content/uploads/2016/01/005-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=RBc5YcuOThY")


disaster = media.Movie("Disaster",
                        "2012 is a 2009 American disaster film directed by Roland Emmerich, and stars John Cusack, Chiwetel Ejiofor, Amanda Peet, Oliver Platt, Thandie Newton, Danny Glover and Woody Harrelson",
                        "https://designmodo.com/wp-content/uploads/2011/02/Creative-Movie-Posters-71.jpg",
                        "https://www.youtube.com/watch?v=rvI66Xaj9-o")

startrek = media.Movie("Star trek",
                        "The USS Enterprise crew explores the furthest reaches of uncharted space, where they encounter a new ruthless enemy who puts them and everything the Federation stands for to the test.",
                        "http://www.printmag.com/wp-content/uploads/star_trek_xi_ver16_xlg.jpg?91875e",
                        "https://www.youtube.com/watch?v=XRVD32rnzOw")



movies = [gamer,jaws,atm,theforest,disaster,startrek]
fresh_tomatoes.open_movies_page(movies)
