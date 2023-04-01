
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.overview_ui import MovieOverviewWidget
from ui.movielist_ui import MovieListWidget
from ui.usersearch_ui import SearchPanel
from ui.time_filter import TimeFilterWidget
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
search_widegt = SearchPanel()
movieslist_widget = MovieListWidget()
overview_widget = MovieOverviewWidget()
timefilter_widget = TimeFilterWidget()

movieslist_widget.movie_clicked.connect(overview_widget.update_movie)
movieslist_widget.update_list(test_movies)

layout = QtWidgets.QVBoxLayout()
layout.addWidget(timefilter_widget)
layout.addWidget(movieslist_widget)
second_page = QtWidgets.QWidget()
second_page.setLayout(layout)

main_window.addWidget(search_widegt)
main_window.addWidget(second_page)
main_window.addWidget(overview_widget)

main_window.resize(800, 600)
main_window.show()

app.exec()
