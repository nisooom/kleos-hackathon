import pandas as pd
import numpy as np
import random
import signal
from src.ui.movieClass import Movie

movie = Movie()







































#

# # def handler(signum, frame):
# #     exit(0)
# #
# #
# dataset = pd.read_csv("../src/ui/clean1.csv")
#
# print(dataset.columns)
# # print(dataset)
#
# # gList = [[i.loc["title"].values, eval(i.loc["Genres"].values) for i in dataset]
# # print(gList)
# #
# g_data = [i for i in dataset.loc[:, :].values]
#
#
# # print(g_data[0])
# #
class Algorithm:
    dataset = pd.read_csv("../playground/clean1.csv")

    g_data = [i for i in dataset.loc[:, :].values]

    def __init__(self):
        self.inputList = []
        self.returnList = []
        self.curr_set = []

    def get_dataset(self, genre: str):
        g_list = []
        for i in self.g_data:
            if genre in eval(i[2]):  # 4 is the genre column
                t = Movie(i[0], i[1], i[3], i[8], eval(i[2]), i[4], eval(i[5]), i[7])
                self.curr_set.append(t)
                g_list.append(t)

        return g_list

    def shuffle(self, i_list):

        if self.curr_set is not None or self.curr_set < i_list:
            for j in range(10):
                t = self.curr_set
                x = random.randint(0, len(t) - 1)
                self.returnList.append(self.curr_set[x])
                self.curr_set.remove(self.curr_set[x])

        return self.returnList
#
#
# # g_d = pd.DataFrame(g_data, columns=["Genre1", "Genre2", "Genre3"])
# # final_dataset = pd.concat([dataset, g_d], axis=1)
# # final_dataset.drop(columns=["Genres"], inplace=True)
# #
# # final_dataset.to_csv("assets/all_cleaned_up.csv")
# # print(g_data)
# #
# # signal.signal(signal.SIGINT, handler)
# #
#
# # needed
# # title, description, rating, imdb link, genres
#
# # columns
# # title', 'rating', 'Genres', 'overview', 'director', 'cast', 'writer','year', 'path'
# #   0       1           2       3           4           5       6       7       8
#
#
# bruh = Algorithm()
# bruh.get_dataset(input("Enter Genre - "))
# bruh_list = bruh.shuffle(10)
#
# while True:
#     print(len(bruh_list))
#     print(len(bruh.curr_set))
#     for i in bruh_list:
#         print(i)
#         print()
#
#     # movies = moviesClass.curr_set
#     # if movies is None:
#     #     break
#     #
#     # print(movies[0])
#     #
#     # yrs5 = 1
#     # yrs10 = 0
#     # yraany = 0
#     #
#     # while movies is not None or len(movies) < 10:
#     #
#     #     # y = movieFrame.sample(n=10, axis="index")
#     #     # print(len(movieFrame))
#     #     #
#     #     # x = movieFrame.drop([i for i in y.index], inplace=True)
#     #
#     #     for j in range(10):
#     #         l = len(movies)
#     #         print(movies[x := random.randint(0, l - 1)])
#     #         movies.remove(movies[x])
#     #         print()
#     #
#     #     # for i in y.values:
#     #     #     if year := i[7] == np.nan or i[7] == 0.0:
#     #     #         continue
#     #     #     x = 0
#     #     #     if x:
#     #     #
#     #     #         if yrs5 == 1 and year > 2018.0:
#     #     #             print(
#     #     #                 f"Title - {i[0]}: Rating - {i[2]}: Genres - {eval(i[3])}: Director - {i[6]}: Cast - {i[5]}: Year - {i[7]} ")
#     #     #         elif yrs10 == 1 and year > 2013.0:
#     #     #             print(
#     #     #                 f"Title - {i[0]}: Rating - {i[2]}: Genres - {eval(i[3])}: Director - {i[6]}: Cast - {i[5]}: Year - {i[7]} ")
#     #     #         elif yraany == 1:
#     #     #             print(
#     #     #                 f"Title - {i[0]}: Rating - {i[2]}: Genres - {eval(i[3])}: Director - {i[6]}: Cast - {i[5]}: Year - {i[7]} ")
#     #     #     else:
#     #     #         print(
#     #     #             f"Title - {i[0]}: Rating - {i[2]}: Genres - {eval(i[3])}: Director - {i[6]}: Cast - {i[5]}: Year - {i[7]} ")
#     #     #
#     #     #     print()
#     #     # # print(len(movieFrame))
#     #     print()
#     #
#     #     if str(input("Continue :")) == "y":
#     #         pass
#     #     else:
#     #         break
#     #
#     #
