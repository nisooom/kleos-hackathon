import numpy
from PyQt5 import QtWidgets, QtGui
from ui.overview_ui import MovieOverviewWidget
from ui.movielist_ui import MovieListWidget
from ui.usersearch_ui import SearchPanel
from ui.time_filter import TimeFilterWidget
from ui.movieClass import Movie
import pandas as pd


dataset = pd.read_csv("src/datasets/clean1.csv")


def get_movies_by_genre(gen):
    if gen == "Select genre":
        return get_movies_by_genre("Action")

    states = timefilter_widget.toggleStates
    flags = [i == "1" for i in states]
    print(flags)

    all_movies = dataset[dataset['Genres'].str.contains(f"{gen}")]
    all_movies['year'] = all_movies.loc[:, 'year'].astype(int)
    print(len(all_movies))

    if flags[0]:
        all_movies = all_movies[all_movies["year"] >= 2017]
        all_movies = all_movies[all_movies["year"] >= 2017]
        print(len(all_movies))
    elif flags[1]:
        all_movies = all_movies[all_movies["year"] >= 2012]
        all_movies = all_movies[all_movies["year"] >= 2012]
        print(len(all_movies))

    # year = dataset['year'].astype(int)
    # print(type(year[0]), year[0])
    # year_movies = dataset['year'].astype(int)>=lowerLimit
    # more_movies = dataset[year_movies]

    some_movies = all_movies.sample(min(len(all_movies), 30))
    # some_movies = some_movies.sort_values(by=["rating"], ascending=False)

    movie_list: list[Movie] = []

    for movie in some_movies.values:
        movie_list.append(Movie(
            title=movie[0],
            rating=str(movie[1]),
            genres=eval(movie[2]),
            desc=movie[3],
            director=movie[4],
            cast=eval(movie[5]),
            year=str(movie[7]),
            imdb_link=movie[8]
        ))

    return movie_list


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

search_widegt.genre_input.currentTextChanged.connect(lambda genre: movieslist_widget.update_list(get_movies_by_genre(genre)))

movieslist_widget.movie_clicked.connect(overview_widget.update_movie)

movieslist_widget.update_list(get_movies_by_genre("Action"))

search_widegt.shuffle_btn.clicked.connect(lambda: movieslist_widget.update_list(get_movies_by_genre(search_widegt.genre_input.currentText())))

timefilter_widget.toggledButton.connect(lambda: movieslist_widget.update_list(get_movies_by_genre(search_widegt.genre_input.currentText())))

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
