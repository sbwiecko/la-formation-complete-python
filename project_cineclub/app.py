from PySide2 import QtWidgets, QtCore

from movie import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies() # ajout du contenu du fichier JSON à l'ouverture du programme
        self.setup_connections()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection) # multiselection
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")
        
        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_removeMovies)

    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)
    
    def populate_movies(self):
        for movie in get_movies():
            #self.lw_movies.addItem(movie.title)
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.movie = movie
            #lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)
    
    def add_movie(self):
        title = self.le_movieTitle.text()
        if not title: return False # ne pas importer une chaine vide

        movie = Movie(title)
        if movie.add_to_movies(): # si bien ajouté à la base de données
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.movie = movie
            #lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)
        
        self.le_movieTitle.setText("") # on efface la ligne

    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems(): # items selection in the listbox
            movie = selected_item.movie
            #movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item)) # based on position

if __name__ == "__main__":
    app = QtWidgets.QApplication([]) # application qui fait tourner les fenêtres
    win = App()
    win.show()
    app.exec_()