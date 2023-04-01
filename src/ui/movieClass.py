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
    year: str

    def __str__(self):
        return f"Title - {self.title}: Rating - {self.rating}: Genres - {self.genres}: Director - {self.director}: Cast - {self.cast}: Year - {self.year}: Desc - {self.desc}"
