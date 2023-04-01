
from PyQt5 import QtWidgets, QtGui, QtCore
from .movieClass import Movie


class MovieOverviewWidget(QtWidgets.QWidget):

    def __init__(self, movie: Movie):
        super().__init__()
        self.movie = movie
        self.setObjectName('overview')
        title_label = QtWidgets.QLabel(movie.title)
        title_label.setObjectName('title')
        rating_label = QtWidgets.QLabel(movie.rating)
        desc_edit = QtWidgets.QPlainTextEdit(movie.desc)
        desc_edit.setObjectName('desc')
        info_edit = QtWidgets.QPlainTextEdit()
        imdb_btn = QtWidgets.QPushButton('IMDb')
        imdb_btn.setObjectName('imdb')
        imdb_btn.setFont(QtGui.QFont('Impact', 45))

        genre_layout = QtWidgets.QHBoxLayout()
        for genre in movie.genres:
            genre_btn = QtWidgets.QPushButton(genre)
            genre_btn.setMaximumWidth(120)
            genre_btn.setDisabled(True)
            genre_layout.addWidget(genre_btn)
            genre_btn.setObjectName('genre')

        info_edit.appendPlainText(f'Director: {movie.director}')
        info_edit.appendPlainText(f'Cast: {", ".join(movie.cast)}')
        info_edit.appendPlainText(f'Released on: {movie.year}')

        title_label.setFont(QtGui.QFont('Inter', 25))
        rating_label.setFont(QtGui.QFont('Inter', 10))
        rating_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        desc_edit.setReadOnly(True)
        info_edit.setReadOnly(True)
        info_edit.setMaximumHeight(70)
        info_edit.setObjectName('cast')
        desc_edit.setFont(QtGui.QFont('Inter', 13))
        imdb_btn.clicked.connect(self.goto_imdb)

        header_layout = QtWidgets.QHBoxLayout()
        header_layout.addWidget(title_label)
        header_layout.addWidget(rating_label)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(header_layout)
        main_layout.addWidget(desc_edit)
        main_layout.addWidget(info_edit)
        main_layout.addLayout(genre_layout)
        main_layout.addWidget(imdb_btn)

        self.setLayout(main_layout)

    def goto_imdb(self) -> None:
        url = f'www.imdb.com{self.movie.imdb_link}'
        print(f'Going to {url!r}')
