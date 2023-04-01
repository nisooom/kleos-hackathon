
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.overview_ui import MovieOverviewWidget
from ui.movielist_ui import MovieListWidget
from ui.usersearch_ui import SearchPanel
from ui.time_filter import TimeFilterWidget
from ui.movieClass import Movie
import pandas as pd


dataset = pd.read_csv("src/datasets/clean1.csv")


def returnList(gen):
    y = dataset['Genres'].str.contains(f"{gen}")
    # if y[1] == True:
    #     print(y)
    x = dataset[y].sample(min(len(y), 20)).values

    """
        Movie Items

        0. Title 0     
        1. Rating 1
        2. Desc 3
        3. IMDBLINE  8
        4. Genre 2
        5. Director 4
        6. Cast 6
        7. Year 7
    """
    movie_list: list[Movie] = []
    for item in x:
        movie_list.append(Movie(
            title=item[0],
            rating=str(item[1]),
            genres=eval(item[2]),
            desc=item[3],
            director=item[4],
            cast=eval(item[5]),
            year=str(int(item[7])),
            imdb_line=item[8]
        ))

    return movie_list


def get_emitter_emit_and_return(genre: str):
    print(genre)
    movieslist_widget.update_list(returnList(genre))



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

search_widegt.genre_input.currentTextChanged.connect(get_emitter_emit_and_return)
movieslist_widget.movie_clicked.connect(overview_widget.update_movie)

# Change this
movieslist_widget.update_list(returnList("Action"))

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
