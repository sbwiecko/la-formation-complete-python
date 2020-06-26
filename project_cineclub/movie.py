import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CUR_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "movies.json")

def get_movies():
    # on récupère la liste des movies et on en créée des instances
    with open(DATA_FILE, 'r') as file:
        return [Movie(movie_title) for movie_title in json.load(file)]

class Movie:
    """
    Class that takes a string and capitalizes it to make the title attribute.
    It also return __repr__ the attribute
    """
    def __init__(self, title):
        try:
            self.title = title.title()
        except:
            print(f"{title} is not a string!")
    
    def __repr__(self):
        return self.title
    
    @classmethod
    def _get_movies(cls):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)

    @classmethod
    def _write_movies(cls, movies):
        with open(DATA_FILE, 'w') as f:
            json.dump(movies, f)
    
    def add_to_movies(self):
        # Récupérer la liste des films
        movies = Movie._get_movies()
        # Vérifier que le film n'est pas déjà dans la liste
        if self.title not in movies:
        # Si ce n'est pas le cas l'ajouter
            movies.append(self.title)
            Movie._write_movies(movies)
            return True
        # Si c'est le cas, on affiche un message pour indiquer
        # que le film est déjà dans la liste (avec le module logging).
        else:
           logging.warning(f"{self.title} is already in movies.json.")
           return False

    def remove_from_movies(self):
        # Récupérer la liste des films
        movies = Movie._get_movies()
        # Vérifier que le film n'est pas déjà dans la liste
        if self.title in movies:
            movies.remove(self.title)
            Movie._write_movies(movies)

if __name__ == "__main__":
   movies = get_movies()
   print(movies[0].title)