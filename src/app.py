
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from dataclasses import dataclass


@dataclass
class MovieItem:
    title: str
    desc: str
    rating: str
    imdb_link: str
    # keywords: list[str]
    # genres: list[str]
    # cast: list[str]


class ListButtons(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.btn1 = QtWidgets.QPushButton('btn-1', self)
        self.btn2 = QtWidgets.QPushButton('btn-2', self)
        self.btn3 = QtWidgets.QPushButton('btn-3', self)
        self.btn4 = QtWidgets.QPushButton('btn-4', self)

class MovieItemUI(QtWidgets.QWidget):

    def __init__(self, item: MovieItem):
        super().__init__()
        uic.loadUi('src/ui/movie_overview_widget.ui', self)
        self.item = item

        self.title_label.setText(item.title)
        self.rating_label.setText(item.rating)
        self.movie_desc.setPlainText(item.desc)
        self.imdb_btn.setText('Go to imdb page')
        self.imdb_btn.clicked.connect(self.goto_imdb)

        area = QtWidgets.QScrollArea()
        area.setWidget(ListButtons())
        self.verticalLayout.addWidget(area)
    
    def goto_imdb(self) -> None:
        print(f'going to imdb.com{self.item.imdb_link}')


app = QtWidgets.QApplication([])

item = MovieItem(
    'Top Gun: Maverick',
    "After more than thirty years of service as one of the Navy's top aviators, Pete Mitchell is where he belongs, pushing the envelope as a courageous test pilot and dodging the advancement in rank that would ground",
    '8.6',
    'youtube.com'
)

win = MovieItemUI(item)
win.show()

app.exec()
