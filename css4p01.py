# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:16:58 2024

@author: NWUUSER
"""

import pandas as pd
df= pd.read_csv("movie_dataset.csv",index_col=0)
# i chose not to delete the rows with "NaN" becuase the information in the other columns might be useful going forward
"""
print(df)
#Q1:Highest rated movies in the dataset
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]

#Answer: Dark of knight with rating of 9.0

#Q2:Average revenue of the all movies in the dataset excluding "NaN"
average_revenue = df['Revenue (Millions)'].mean(skipna=True)
print(f"The average revenue of all movies (excluding NaN values) is: {average_revenue}")
#answer =82.95637614678898 millions


#Q3:
# Filter the DataSet for movies released between 2015 and 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue for movies in the specified years
average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

# Print the result
print(f"The average revenue for movies released from 2015 to 2017 is: {average_revenue_2015_to_2017}")
#Answer: 63.099905660377345 millions


#Q4: Number of movies released in 2016
# Filter the DataSet for movies released in 2016
movies_2016 = df[df['Year'] == 2016]

# Count the number of movies in 2016
num_movies_2016 = len(movies_2016)

# Print the result
print(f"The number of movies released in 2016 is: {num_movies_2016}")
#answer= 297

#Question 5:Movies directed by Christpher Nolan
# Filter the Dataset for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Count the number of movies directed by Christopher Nolan
num_nolan_movies = len(nolan_movies)

# Print the result
print(f"The number of movies directed by Christopher Nolan is: {num_nolan_movies}")
#Answer=5

#Question 6:Movies with rating of atleast 8.0
# Filter the DataSet for movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]

# Count the number of movies with a rating of at least 8.0
num_high_rated_movies = len(high_rated_movies)

# Print the result
print(f"The number of movies with a rating of at least 8.0 is: {num_high_rated_movies}")
#Answer:78

#Q7: Median rating of the Christopher Nolan Movies
# Filter the DataFrame for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median of ratings for Christopher Nolan movies
median_rating_nolan_movies = nolan_movies['Rating'].median()

# Print the result
print(f"The median rating of movies directed by Christopher Nolan is: {median_rating_nolan_movies}")
#Answer=8.6

#Question 8: Year with the highest average rating
# Group the DataSet by 'Year' and calculate the average rating for each year
average_rating_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

# Print the result
print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}")
#Answer=7.13 in 2006


#Question 9: the number of increse in percentage of movies made between 2006 and 2016
# Count the number of movies made in 2006 and 2016
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

# Print the result
print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")
#Answer=575.00%

#Question 10: Most common actor
# Split the 'Actors' column by commas and stack the resulting lists into individual rows
actor_df = df['Actors'].str.split(',').explode()

# Remove leading and trailing whitespaces from actor names
actor_df = actor_df.str.strip()

# Find the most common actor
most_common_actor = actor_df.mode().values[0]

# Count the occurrences of the most common actor
num_occurrences = actor_df.value_counts().max()

# Print the result
print(f"The most common actor is '{most_common_actor}' with {num_occurrences} occurrences.")
#Answer 'Mark Wahlberg' with 15 occurrences

#Question 11" Unique genres
# Split the 'Genre' column by commas and stack the resulting lists into individual rows
genre_df = df['Genre'].str.split(',').explode()

# Remove leading and trailing whitespaces from genre names
genre_df = genre_df.str.strip()

# Count the number of unique genres
num_unique_genres = genre_df.nunique()

# Print the result
print(f"The number of unique genres is: {num_unique_genres}")
#Answer=20
"""
#Question 12: Do a correlation of the numerical features
import seaborn as sns
import matplotlib.pyplot as plt
# Drop non-numeric columns for simplicity in this example
numeric_columns = df.select_dtypes(include='number')

# Calculate the correlation matrix
correlation_matrix = numeric_columns.corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Create a Seaborn heatmap with correlation values
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)

# Show the plot
plt.title("Correlation Heatmap")
plt.show()
#From the heat plot, highest correlation is found between vote and Revenue (0.640), metascore and rating (0.63) and rating and votes(0.510)
#It seems the more money spend on movie, the more votes it got however the revenue doesnt necessarily result in a high rating. People hate movings that have long runtime seeing the correlation of 0.39.



















































