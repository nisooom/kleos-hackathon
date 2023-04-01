
from PyQt5 import QtWidgets, QtGui, QtCore
from .movieClass import Movie


class MovieCardItem(QtWidgets.QWidget):

    def __init__(self, movie: Movie, parent: 'MovieListWidget'):
        super().__init__(parent)
        self.movie = movie
        self.list = parent
        
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

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.list.movie_clicked.emit(self.movie)
        return super().mousePressEvent(event)


class MovieListWidget(QtWidgets.QScrollArea):
    movie_clicked = QtCore.pyqtSignal(Movie)

    def update_list(self, movies: list[Movie]):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        for movie in movies:
            layout.addWidget(MovieCardItem(movie, self))
        widget.setLayout(layout)
        self.setWidget(widget)
