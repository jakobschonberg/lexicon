#B1
movie_dictionary = {"title": "Monty Python and the Holy Grail",
                    "director": "Terry Gilliam & Terry Jones",
                    "rating": 8.1 
                    }

#B2, B3
class Movie():
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_highly_rated(self):
        return self.rating >= 8

movie = Movie("Monty Python and the Holy Grail", "Terry Gilliam & Terry Jones", 8.1)
print(movie.is_highly_rated())

#B4
#I would choose dictionary if I'm making one and only one object of its kind
#I would choose a class if I'm making at least two objects that needs to have the same attributes/behaviour

