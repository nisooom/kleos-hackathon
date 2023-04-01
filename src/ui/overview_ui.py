
from PyQt5 import QtWidgets, QtGui, QtCore
from .movieClass import Movie


class MovieOverviewWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName('overview')
        self.title_label = QtWidgets.QLabel()
        self.title_label.setObjectName('title')
        self.rating_label = QtWidgets.QLabel()
        self.desc_edit = QtWidgets.QPlainTextEdit()
        self.desc_edit.setObjectName('desc')
        self.info_edit = QtWidgets.QPlainTextEdit()
        self.imdb_btn = QtWidgets.QPushButton('IMDb')
        self.imdb_btn.setObjectName('imdb')
        self.imdb_btn.setFont(QtGui.QFont('Impact', 45))

        self.movie = None

        self.genre_layout = QtWidgets.QHBoxLayout()

        self.title_label.setFont(QtGui.QFont('Inter', 25))
        self.rating_label.setFont(QtGui.QFont('Inter', 10))
        self.rating_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.desc_edit.setReadOnly(True)
        self.info_edit.setReadOnly(True)
        self.info_edit.setMaximumHeight(70)
        self.info_edit.setObjectName('cast')
        self.desc_edit.setFont(QtGui.QFont('Inter', 13))
        self.imdb_btn.clicked.connect(self.goto_imdb)

        header_layout = QtWidgets.QHBoxLayout()
        header_layout.addWidget(self.title_label)
        header_layout.addWidget(self.rating_label)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.desc_edit)
        main_layout.addWidget(self.info_edit)
        main_layout.addLayout(self.genre_layout)
        main_layout.addWidget(self.imdb_btn)

        self.setLayout(main_layout)

    def update_movie(self, movie: Movie) -> None:
        self.title_label.setText(movie.title)
        self.rating_label.setText(movie.rating)
        self.desc_edit.setPlainText(movie.desc)
        self.info_edit.clear()
        self.movie = movie

        items = [self.genre_layout.itemAt(i) for i in range(self.genre_layout.count())]
        for item in items:
            item.widget().setParent(None)

        for genre in movie.genres:
            genre_btn = QtWidgets.QPushButton(genre)
            genre_btn.setMaximumWidth(120)
            genre_btn.setDisabled(True)
            genre_btn.setObjectName('genre')
            self.genre_layout.addWidget(genre_btn)

        self.info_edit.appendPlainText(f'Director: {movie.director}')
        self.info_edit.appendPlainText(f'Cast: {", ".join(movie.cast)}')
        self.info_edit.appendPlainText(f'Released on: {movie.year}')

    def goto_imdb(self) -> None:
        if self.movie is None:
            return

        url = f'www.imdb.com{self.movie.imdb_line}'
        print(f'Going to {url!r}')
