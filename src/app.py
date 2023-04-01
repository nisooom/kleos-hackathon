
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.overview_ui import MovieOverviewWidget
from ui.movielist_ui import MovieListWidget
from ui.movieClass import Movie
from ui.randomData import test_movies


app = QtWidgets.QApplication([])
qss_stylesheet = open('src/index.css').read()
app.setStyleSheet(qss_stylesheet)

QtGui.QFontDatabase.addApplicationFont('assets/fonts/static/Inter-Regular.ttf')

main_window = QtWidgets.QSplitter()

overview_widget = MovieOverviewWidget(test_movies[0])
main_window.addWidget(overview_widget)

moveslist_widget = MovieListWidget()
moveslist_widget.update_list(test_movies)
main_window.addWidget(moveslist_widget)

main_window.resize(800, 600)
main_window.show()

app.exec()
