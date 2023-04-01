
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.overview_ui import MovieOverviewWidget
from ui.movielist_ui import MovieListWidget
from ui.usersearch_ui import SearchPanel
from ui.time_filter import TimeFilterWidget
from ui.movieClass import Movie
import pandas as pd


dataset = pd.read_csv("src/datasets/clean1.csv")


def returnList(gen):
    if gen == "Select genre":
        return returnList("Action")

    all_movies = dataset['Genres'].str.contains(f"{gen}")
    some_movies = dataset[all_movies].sample(min(len(all_movies), 30))
    some_movies = some_movies.sort_values(by=["rating"], ascending=False)
    movie_list: list[Movie] = []
    for movie in some_movies.values:
        movie_list.append(Movie(
            title=movie[0],
            rating=str(movie[1]),
            genres=eval(movie[2]),
            desc=movie[3],
            director=movie[4],
            cast=eval(movie[5]),
            year=str(int(movie[7])),
            imdb_link=movie[8]
        ))

    return movie_list


def get_emitter_emit_and_return(genre: str):
    if genre is None:
        print("here")
        movieslist_widget.update_list(returnList("Action"))
    else:
        movieslist_widget.update_list(returnList(genre))

    print(genre)


app = QtWidgets.QApplication([])
stylesheet = open('src/index.css').read()
app.setStyleSheet(stylesheet)

main_window = QtWidgets.QSplitter()

main_window.setWindowTitle('Movie Mentor - Kleos Hackathon')
window_icon = QtGui.QIcon('assets/MovieMentorLogo.png')
main_window.setWindowIcon(window_icon)

search_widegt = SearchPanel()
movieslist_widget = MovieListWidget()
overview_widget = MovieOverviewWidget()
timefilter_widget = TimeFilterWidget()

search_widegt.genre_input.currentTextChanged.connect(get_emitter_emit_and_return)

movieslist_widget.movie_clicked.connect(overview_widget.update_movie)

movieslist_widget.update_list(returnList("Action"))

search_widegt.shuffle_btn.clicked.connect(lambda: get_emitter_emit_and_return(search_widegt.genre_input.currentText()))



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
