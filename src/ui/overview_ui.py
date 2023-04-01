
from PyQt5 import QtWidgets, QtGui, QtCore
from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    desc: str
    rating: str
    imdb_link: str
    genres: list[str]
    director: str
    cast: list[str]
    year: str


class MovieOverviewWidget(QtWidgets.QWidget):

    def __init__(self, movie: Movie):
        super().__init__()
        self.movie = movie

        title_label = QtWidgets.QLabel(movie.title)
        rating_label = QtWidgets.QLabel(movie.rating)
        desc_edit = QtWidgets.QPlainTextEdit(movie.desc)
        info_edit = QtWidgets.QPlainTextEdit()
        imdb_btn = QtWidgets.QPushButton('Go to IMDB page')

        genre_layout = QtWidgets.QHBoxLayout()
        for genre in movie.genres:
            genre_btn = QtWidgets.QPushButton(genre)
            genre_btn.setMaximumWidth(120)
            genre_btn.setDisabled(True)
            genre_layout.addWidget(genre_btn)

        info_edit.appendPlainText(f'Director: {movie.director}')
        info_edit.appendPlainText(f'Cast: {", ".join(movie.cast)}')
        info_edit.appendPlainText(f'Released on: {movie.year}')

        title_label.setFont(QtGui.QFont('Arial', 25))
        rating_label.setFont(QtGui.QFont('Arial', 10))
        rating_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        desc_edit.setReadOnly(True)
        info_edit.setReadOnly(True)
        info_edit.setMaximumHeight(70)
        desc_edit.setFont(QtGui.QFont('Arial', 13))
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



if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    item = Movie(
        'Top Gun: Maverick',
        "After more than thirty years of service as one of the Navy's top aviators, Pete Mitchell is where he belongs, pushing the envelope as a courageous test pilot and dodging the advancement in rank that would ground",
        '8.6',
        '/title/tt98492',
        ['action', 'suspense', 'more-shit', 'rom'],
        'Mr Director',
        ['NAME-1', 'name-2', 'name-3'],
        '2014'
    )

    win = MovieOverviewWidget(item)
    win.show()

    app.exec()
