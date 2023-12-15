import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


anime_data = pd.read_csv('./data/anime.csv')
#print(anime_data)

user_ratings = pd.read_csv('./data/rating.csv')

genres_dummies = anime_data['genre'].str.join('|').str.get_dummies()

anime_data = pd.concat([anime_data, genres_dummies], axis=1)
print(anime_data)