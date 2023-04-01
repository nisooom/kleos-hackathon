import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
df = pd.read_csv('./Movie_Dataset.csv')

# Rename columns
df = df.rename(columns={'movie title': 'title',
                        'Run Time': 'duration',
                        'Rating': 'rating',
                        'User Rating': 'user_count',
                        'Generes': 'Genres',
                        'Overview': 'overview',
                        'Plot Kyeword': 'keywords',
                        'Director': 'director',
                        'Top 5 Casts': 'cast',
                        'Writer': 'writer',
                        })

# Remove duplicate elements
df = df.loc[~df.duplicated(subset=['title', 'year'])]\
    .reset_index(drop=True).copy()


# Make all movie earnings into NaN [OLD APPROACH]
# df.loc[df["duration"].str.startswith("$"), 'duration'] = "0"
# df.loc[df["duration"].str.startswith("₹"), 'duration'] = "0"
# df.loc[df["duration"].str.startswith("£"), 'duration'] = "0"

# function to check if there is duration of the movie


def has_hours_minutes(row):
    duration = row['duration']
    if 'hour' in duration and 'minute' in duration:
        return True
    elif 'hour' not in duration and 'minute' in duration:
        return True
    elif 'hour' in duration and 'minute' not in duration:
        return True
    else:
        return False


# Filter out elements that have Time and set others to NaN
filtered_df = df[df.apply(has_hours_minutes, axis=1)]
df.loc[~df.index.isin(filtered_df.index), 'duration',] = np.nan

# Clean years from the dataset
df['year'] = df.year.str.extract('(\d+)')


# Cleaning Unreleased films
unReleased = df[df["duration"].str.contains("not-released") == True]
df.drop([i for i in unReleased.index], axis="index", inplace=True)
df.drop("keywords", axis='columns', inplace=True)

noData = df[df["overview"].isna()]
df.drop([i for i in noData.index], axis='index', inplace=True)

unRated = df[df["rating"].str.contains("no-rating") == True]

df.drop([i for i in unRated.index], axis='index', inplace=True)
df.drop("user_count", axis='columns', inplace=True)
# Datatype conversion [doesnt work as null values are double and making values float give trailing numbers]
df['rating'] = df['rating'].astype('str')
df.drop("duration", axis='columns', inplace=True)

nanYears = df[df["year"].isna()]
df.drop([i for i in nanYears.index], axis='index', inplace=True)


df.to_csv("./clean1.csv", index=False)
