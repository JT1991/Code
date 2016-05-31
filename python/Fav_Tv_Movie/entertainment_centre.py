# Importing media and tomatoes classes
import fresh_tomatoes
import media

# Creating instances of Movie
the_departed = media.Movie("The Departed",
                           "An undercover cop and a mole in the police\
                            attempt to identify each other while\
                            infiltrating an Irish gang in South Boston.",
                           "https://c2.staticflickr.com/6/5257/5430944730_8842851d47_b.jpg",  # noqa
                           "https://www.youtube.com/watch?v=SGWvwjZ0eDc",
                           "http://www.oocities.org/escottish144/Images/PastRating18_large.gif")  # noqa

plup_fiction = media.Movie("Pulp Fiction",
                           "The lives of two mob hit men, a boxer, a gangster's\
                           wife, and a pair of diner bandits intertwine in \
                           four tales of violence and redemption.",
                           "http://www.swotti.com/tmp/swotti/cacheCHVSCCBMAWN0AW9URW50ZXJ0YWLUBWVUDC1NB3ZPZXM=/imgPulp%20fiction1.jpg",  # noqa
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
                           "http://www.oocities.org/escottish144/Images/PastRating18_large.gif")  # noqa

usual_suspects = media.Movie("Usual Suspects",
                             "Who is Keyzer Soze?",
                             "http://t1.gstatic.com/images?q=tbn:ANd9GcRhueZ4Pye4T080t9Qj_aIQhTpilYjUReiszdvS2Vm_XgkvnfWA",  # noqa
                             "https://www.youtube.com/watch?v=9MjV4EwR7Mg",
                             "http://www.oocities.org/escottish144/Images/PastRating15_large.gif")  # noqa

leon = media.Movie("Leon", "A perfect assassin. An innocent girl. They have \
                   nothing left to lose except each other. ",
                   "http://www.impawards.com/1994/posters/professional_ver1.jpg",  # noqa
                   "https://www.youtube.com/watch?v=Dc1KzpMnuX0",
                   "http://www.oocities.org/escottish144/Images/PastRating15_large.gif")  # noqa


rosen_guild = media.Movie("Rosencrantz & Guildenstern",
                          "Two minor characters from the play, 'Hamlet' stumble\
                          around unaware of their scripted lives.",
                          "http://ia.media-imdb.com/images/M/MV5BNjc0MTU0MDY1OV5BMl5BanBnXkFtZTcwMDI2OTY2NA@@._V1_SX640_SY720_.jpg",  # noqa
                          "https://www.youtube.com/watch?v=LBfFYvdfL90",
                          "http://www.oocities.org/escottish144/Images/PastRatingPG_large.gif")  # noqa

children_of_men = media.Movie("Children of Men",
                              "In 2027, in a chaotic world in which women have \
                              become somehow infertile, a former activist \
                              agrees to help transport a miraculously pregnant\
                               woman to a sanctuary at sea.",
                              "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5O7kC8EwYpKjy8zKDBWXRSjCBU2afIWVVYFx6v5Wvy4uW3wjjaA",  # noqa
                              "https://www.youtube.com/watch?v=Q9CFcTY_pik",
                              "http://www.oocities.org/escottish144/Images/PastRating15_large.gif")  # noqa

hot_fuzz = media.Movie("Hot Fuzz",
                       "Exceptional London cop Nicholas Angel is involuntarily\
                       transferred to a quaint English village and paired with\
                       a witless new partner. While on the beat, Nicholas \
                       suspects a sinister conspiracy is afoot with \
                       the residents.",
                       "https://www.movieposter.com/posters/archive/main/68/MPW-34310",  # noqa
                       "https://www.youtube.com/watch?v=ayTnvVpj9t4",
                       "http://www.bbfc.co.uk/sites/default/files/styles/100x/public/certificate/BBFC_15_150px-height_0.png?itok=psbQdb1L")  # noqa

blade_run = media.Movie("Blade Runner",
                        "A blade runner must pursue and try to terminate four \
                        replicants who stole a ship in space and have returned\
                        to Earth to find their creator.",
                        "https://candykiller.files.wordpress.com/2014/02/bladerunner.png",  # noqa
                        "https://www.youtube.com/watch?v=4lW0F1sccqk",
                        "http://www.bbfc.co.uk/sites/default/files/styles/100x/public/certificate/BBFC_15_150px-height_0.png?itok=psbQdb1L")  # noqa

seven = media.Movie("Se7en",
                    "Two detectives, a rookie and a veteran, hunt a serial \
                    killer who uses the seven deadly sins as his modus \
                    operandi.",
                    "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRkcRBS7f2pF68h--Aew49p_3GpEj7ECX7QIQQ4hfbtZ_vqGEw8",  # noqa
                    "https://www.youtube.com/watch?v=J4YV2_TcCoE",
                    "http://www.bbfc.co.uk/sites/default/files/styles/100x/public/certificate/BBFC_18_150px-height_0.png?itok=6PG01tHh")  # noqa

birdman = media.Movie("Birdman",
                      "Illustrated upon the progress of his latest Broadway \
                      play, a former popular actor's struggle to cope with his\
                      current life as a wasted actor is shown. ",
                      "http://www.superherohype.com/assets/uploads/2014/09/a_900x0.jpg",  # noqa
                      "https://www.youtube.com/watch?v=uJfLoE6hanc",
                      "http://www.bbfc.co.uk/sites/default/files/styles/100x/public/certificate/BBFC_15_150px-height_0.png?itok=psbQdb1L")  # noqa

# Creating instances of Tv_Show

game_thrones = media.Tv_Show("Game Of Thrones",
                             "While a civil war brews between several noble \
                             families in Westeros, the children of the former \
                             rulers of the land attempt to rise up to power.",
                             "https://s-media-cache-ak0.pinimg.com/564x/01/1e/c4/011ec4306a21ef21372e83bb36a2451e.jpg",  # noqa
                             "https://www.youtube.com/watch?v=6MophfvUlfI",
                             "6")

orphan_black = media.Tv_Show("Orphan Black",
                             " A streetwise hustler is pulled into a compelling\
                             conspiracy after witnessing the suicide of a girl\
                             who looks just like her.",
                             "http://vignette2.wikia.nocookie.net/orphanblack/images/3/39/Orphan-Black-Season-1-Promo-Poster.jpg/revision/latest?cb=20150828074008",  # noqa
                             "https://www.youtube.com/watch?v=i-UEa_BIHqU",
                             "4")

misfits = media.Tv_Show("Misfits",
                        " A group of young offenders doing community service \
                        get struck by lightning during a storm, and begin to \
                        develop superpowers.",
                        "http://s.sidereel.com/tv_shows/42441/giant_2x/VSC_Misfits-compressor.jpg",  # noqa
                        "https://www.youtube.com/watch?v=nTeGvifpVZU",
                        "5")

wire = media.Tv_Show("The Wire", "Baltimore drug scene, seen through the eyes \
                     of drug dealers and law enforcement.",
                     "https://dvdbash.files.wordpress.com/2013/06/poster-the-wire-tv-series-s2-3-dvdbash-wordpress.jpg",  # noqa
                     "https://www.youtube.com/watch?v=apZQlqPp6Hs",
                     "5")

black_books = media.Tv_Show("Black books",
                            "Misadventures of a alcholic second-hand book \
                            seller, who hates selling books.",
                            "http://ecx.images-amazon.com/images/I/51YfDmh7eUL.jpg",  # noqa
                            "https://www.youtube.com/watch?v=Q2bNMIeBLcM",
                            "3")

xfiles = media.Tv_Show("The X-files",
                       " Two FBI agents, Fox Mulder the believer and Dana\
                       Scully the skeptic, investigate the strange and\
                       unexplained while hidden forces work to impede their\
                       efforts. ",
                       "http://ecx.images-amazon.com/images/I/913rKROFf3L._SL1500_.jpg",  # noqa
                       "https://www.youtube.com/watch?v=mlZIVpVNgpI",
                       "9")


# Creating list of movies
movies = [the_departed, usual_suspects, plup_fiction, leon, rosen_guild,
          children_of_men, blade_run, seven, birdman]
# Creating list of tv shows
tv_shows = [game_thrones, orphan_black, misfits, wire, black_books, xfiles]
# Opening the movies html page
fresh_tomatoes.save_tv_page(tv_shows)
fresh_tomatoes.open_movies_page(movies)
