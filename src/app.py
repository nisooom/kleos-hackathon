import numpy
from PyQt5 import QtWidgets, QtGui
from ui.overview_ui import MovieOverviewWidget
from ui.movielist_ui import MovieListWidget
from ui.usersearch_ui import SearchPanel
from ui.time_filter import TimeFilterWidget
from ui.movieClass import Movie
import pandas as pd


dataset = pd.read_csv("src/datasets/clean1.csv")


def update_list():
    genre = search_widegt.genre_input.currentText()
    time_flags = [i == "1" for i in timefilter_widget.toggleStates]

    if genre == 'Select genre':
        genre = 'Action'

    all_movies = dataset[dataset['Genres'].str.contains(f"{genre}")]
    all_movies['year'] = all_movies.loc[:, 'year'].astype(int)

    if time_flags[0]:
        all_movies = all_movies[all_movies["year"] >= 2017]
    elif time_flags[1]:
        all_movies = all_movies[all_movies["year"] >= 2012]

    some_movies = all_movies.sample(min(len(all_movies), 30))
    movies_list: list[Movie] = []
    for movie in some_movies.values:
        movies_list.append(Movie(
            title=movie[0],
            rating=str(movie[1]),
            genres=eval(movie[2]),
            desc=movie[3],
            director=movie[4],
            cast=eval(movie[5]),
            year=str(movie[7]),
            imdb_link=movie[8]
        ))
    
    movieslist_widget.update_list(movies_list)


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


update_list()
movieslist_widget.movie_clicked.connect(overview_widget.update_movie)

search_widegt.genre_input.currentTextChanged.connect(update_list)
search_widegt.shuffle_btn.clicked.connect(update_list)
timefilter_widget.buttonClicked.connect(update_list)

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
