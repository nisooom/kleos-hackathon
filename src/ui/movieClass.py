from dataclasses import dataclass
import pandas as pd
import random

@dataclass
class Movie:

    title: str
    rating: str
    desc: str
    imdb_line: str
    genres: list[str]
    director: str
    cast: list[str]
    year: float

    def __str__(self):
        return f"Title - {self.title}: Rating - {self.rating}: Genres - {self.genres}: Director - {self.director}: Cast - {self.cast}: Year - {self.year}: Desc - {self.desc}"


class Algorithm:
    dataset = pd.read_csv("clean1.csv")

    g_data = [i for i in dataset.loc[:, :].values]
    curr_set = []

    def __init__(self):
        self.inputList = []
        self.returnList = []

    def get_dataset(self, genre: str):
        g_list = []
        for i in self.g_data:
            if genre in eval(i[2]):  # 4 is the genre column
                t = Movie(i[0], i[1], i[3], i[8], eval(i[2]), i[4], eval(i[5]), i[7])
                self.curr_set.append(t)
                g_list.append(t)

        return g_list

    def shuffle(self, genre, i_list):
        self.inputList = self.get_dataset(genre)

        if self.curr_set is not None or self.curr_set < i_list:
            for j in range(10):
                t = self.curr_set
                x = random.randint(0, len(t) - 1)
                self.returnList.append(self.curr_set[x])
                self.inputList.remove(self.curr_set[x])

        return self.returnList
