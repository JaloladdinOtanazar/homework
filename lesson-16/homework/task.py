# Part 1
import sqlite3
import pandas as pd 
import json
# 1st
con = sqlite3.connect('chinook.db')
df_customers = pd.read_sql_query('SELECT * FROM customers', con)
first_ten_rows = df_customers.head(10)
print(first_ten_rows)
print('-'*200, '\n')
# 2nd
read = pd.read_json('iris.json')
shape = read.shape
columns = read.columns
print(columns, shape)
print('-'*200, '\n')
# 3rd
data = pd.read_excel('titanic.xlsx')
first_5_rows = data.head()
print(first_5_rows)
print('-'*200, '\n')
# 4th
flights = pd.read_parquet('flights.htm')
info = flights.info
print(info)
print('-'*200, '\n')

#5th
movie_data = pd.read_csv('movie.csv')
sample = movie_data.sample(10)
print(sample)
print('-'*200, '\n')

# Part 2
# 1st
read = pd.read_json('iris.json')
new_column = (column.lower() for column in read.columns)
read.columns = new_column
print(read.columns)
df_selected = read[['sepallength', 'sepalwidth']]
print(df_selected)
print('-'*200, '\n')

#2nd
from collections import Counter
data_selected = data[data['Age'] > 30]
sex_count = Counter(data["Sex"])
print(data_selected)
print(sex_count)
print('-'*200, '\n')
# 3rd
flights_data = flights[['origin', 'dest', 'carrier']]
unique_dest = flights['dest'].nunique()
print(flights_data)
print(unique_dest)
print('-'*200, '\n')
#4th 
movie_data_filtered = movie_data[movie_data['duration'] > 120]
sorted = movie_data_filtered.sort_values(by=['duration'], ascending=False)
print(movie_data_filtered, '\n')
print(sorted, '\n')
print('-'*200, '\n')
# Part 3
# 1st
numerical_mean =read.mean(numeric_only=True)
numerical_median = read.median(numeric_only=True)
numerical_std = read.std(numeric_only=True)
print(f'mean of each numerical column:\n{numerical_mean}')
print(f'median of each numerical column:\n{numerical_median}')
print(f'std of each numerical column:\n{numerical_std}')
print('-'*200, '\n')
#2nd
min_titanic_age = min(data['Age'])
max_titanic_age = max(data['Age'])
sum_titanic_age = sum(data['Age'])
print(f'minimum of passenger ages:\n{min_titanic_age}')
print(f'maximum of passenger ages:\n{max_titanic_age}')
print(f'sum of passenger ages:\n{sum_titanic_age}')
print('-'*200, '\n')
#3nd
max_likes_row = movie_data.loc[movie_data['director_facebook_likes'].idxmax()]
director_with_highest_likes = max_likes_row['director_name']
his_highest_like = max_likes_row['director_facebook_likes']
movies = movie_data[['movie_title', 'director_name', 'duration']].sort_values(by=['duration'], ascending=True).head()
print(f' Director with most facebook likes is {director_with_highest_likes} with number of like({his_highest_like})')
print(f'5 longest movies with its title, director, and duration respestively:\n{movies}')
# 4th
missing_values = flights.isnull()
mean_of_column = flights['flight duration'].mean()
flights['flight duration'].fillna(mean_of_column, inplace=True)