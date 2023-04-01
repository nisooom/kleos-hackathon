
from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    rating: str
    desc: str
    director: str
    genres: list[str]
    cast: list[str]
    imdb_link: str
    year: str
