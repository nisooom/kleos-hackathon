
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.overview_ui import MovieOverviewWidget
from ui.movielist_ui import MovieListWidget
from ui.movieClass import Movie
from ui.randomData import test_movies


def load_stylesheet():
    qss_stylesheet = open('src/index.css').read()
    app.setStyleSheet(qss_stylesheet)


app = QtWidgets.QApplication([])
load_stylesheet()

QtGui.QFontDatabase.addApplicationFont('assets/fonts/static/Inter-Regular.ttf')

watcher = QtCore.QFileSystemWatcher(['src/index.css'])
watcher.fileChanged.connect(load_stylesheet)

main_window = QtWidgets.QSplitter()

overview_widget = MovieOverviewWidget()
main_window.addWidget(overview_widget)

moveslist_widget = MovieListWidget()
moveslist_widget.movie_clicked.connect(overview_widget.update_movie)
moveslist_widget.update_list(test_movies)
main_window.addWidget(moveslist_widget)

main_window.resize(800, 600)
main_window.show()

app.exec()
