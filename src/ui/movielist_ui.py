
from PyQt5 import QtWidgets, QtGui, QtCore
from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    desc: str
    # rating: str
    # imdb_link: str
    genres: list[str]
    # director: str
    # cast: list[str]
    # year: str


class MovieCardItem(QtWidgets.QWidget):

    def __init__(self, movie: Movie):
        super().__init__()
        
        title_label = QtWidgets.QLabel(movie.title)
        desc_label = QtWidgets.QLabel(movie.desc)
        genre_label = QtWidgets.QLabel(' '.join(movie.genres))

        title_label.setObjectName('listTitleLabel')
        desc_label.setObjectName('listDescLabel')
        genre_label.setObjectName('listGenreLabel')

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addWidget(desc_label)
        main_layout.addWidget(genre_label)
        main_layout.setSpacing(5)
        self.setLayout(main_layout)


class MovieListWidget(QtWidgets.QScrollArea):

    def update_list(self, movies: list[Movie]):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        for movie in movies:
            layout.addWidget(MovieCardItem(movie))
        widget.setLayout(layout)
        self.setWidget(widget)



movies = [
    Movie('Movie -1', 'Once upon a time there lived an asshole', ['Comedy', 'Adventure', 'Drama']),
    Movie('Movie -2', 'Once upon a time there lived an guy', ['Action', 'Adventure', 'Drama']),
    Movie('Movie -3', 'Once upon a time there lived an girl', ['Romance', 'Adventure', 'Drama']),
    Movie('Movie -4', 'Once upon a time there lived an couple', ['Suspense', 'Crime', 'Drama']),
] * 5

app = QtWidgets.QApplication([])
app.setStyleSheet('''
''')

area = MovieListWidget()
area.update_list(movies)
area.resize(800, 600)
area.show()

app.exec()
