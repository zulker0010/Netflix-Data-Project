import numpy as np 
import pandas as pd 
import matplotlib.pyplot as pt 
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer 
from seaborn import load_dataset

#navigate file path & read dataset
file_path = ("E:\\Analytics\\data projects\\Netflix-Data-Project\\titles.csv")
dataset = pd.read_csv(file_path)

#drop the first column containing content ID
dataset.drop(columns=dataset.columns[0], inplace=True)
new_df = dataset.drop(columns=dataset.columns[0]) 
new_df.head()

#classify based on content type
category_list = 'type'
split_text = 'MOVIE'
#boolean masks based on text comparison
mask_1 = new_df[category_list].str.contains(split_text)
mask_2 = ~ mask_1
df_movies = new_df[mask_1]
df_shows = new_df[mask_2]
print(df_movies)
print(df_shows)

#fill the missing values in column 8:11
fill_columns = ['imdb_score','imdb_votes','tmdb_popularity','tmdb_score']
df_movies[fill_columns] = df_movies[fill_columns].fillna(df_movies[fill_columns].mean())
df_shows[fill_columns] = df_shows[fill_columns].fillna(df_shows[fill_columns].mean())

#drop 'seasons' column for the df_movies dataframe
df_movies.drop(columns = df_movies.columns[6], inplace = True)
df_movies0 = df_movies.drop(columns = df_movies.columns[6])

#export new dataframes into an excel file
df_movies.to_excel('df_movies.xlsx', index = False)
df_shows.to_excel('df_shows.xlsx', index = False)

#one_hot_encoding on the new_df
transformer = make_column_transformer(
 (OneHotEncoder(), [0]),
  remainder = 'passthrough'
 )
transformed = transformer.fit_transform(new_df)
new_df = transformed
print(new_df)

DF = pd.DataFrame(new_df)
DF.to_excel('new_df.xlsx', index = False)
