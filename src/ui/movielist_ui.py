
from typing import Optional
from PyQt5 import QtWidgets, QtGui, QtCore
from .movieClass import Movie


# TEJAS RIGHT HERE
DEFAULT_STYLESHEET = '''
QWidget{
color:#8f8f8f;
padding-top:5;
padding-right:5;
padding-left:5;
background-color:##1a1a1a;
}
'''
SELECTED_STYLESHEET = '''
QWidget{
padding-top:5;
padding-right:5;
padding-left:5;
color:#d4d4d4;
background-color:#1c1c1c;
}
'''


class MovieCardItem(QtWidgets.QWidget):

    def __init__(self, movie: Movie, parent: 'MovieListWidget'):
        super().__init__(parent)
        self.movie = movie
        self.list = parent
        self.setStyleSheet(DEFAULT_STYLESHEET)
        
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
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.list.update_selected(self)
            self.list.movie_clicked.emit(self.movie)
        return super().mousePressEvent(event)


class MovieListWidget(QtWidgets.QScrollArea):
    movie_clicked = QtCore.pyqtSignal(Movie)

    def __init__(self):
        super().__init__()
        self.selected_card: Optional[MovieCardItem] = None

    def update_selected(self, card: MovieCardItem) -> None:
        if self.selected_card is not None:
            self.selected_card.setStyleSheet(DEFAULT_STYLESHEET)
        self.selected_card = card
        self.selected_card.setStyleSheet(SELECTED_STYLESHEET)

    def update_list(self, movies: list[Movie]):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        for movie in movies:
            layout.addWidget(MovieCardItem(movie, self))
        widget.setLayout(layout)
        self.setWidget(widget)
