import numpy as np 
import pandas as pd 
import matplotlib.pyplot as pt 

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

