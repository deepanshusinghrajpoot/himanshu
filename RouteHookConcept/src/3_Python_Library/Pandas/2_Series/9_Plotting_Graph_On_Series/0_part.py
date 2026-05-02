import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os




# ==================================================
# Visualization with Pandas Series
# ==================================================

# Definition (Interview Friendly)
# Pandas Series provides built-in plotting functionality
# using the Matplotlib library to visualize data quickly.

# Important Points
# • Pandas internally uses Matplotlib for plotting
# • Series.plot() is used for creating graphs
# • Different graph types can be created using the "kind" parameter
# • Visualization helps in understanding data patterns easily



path_dir = os.path.dirname(__file__)
file_path1 = os.path.join(path_dir, '../../1_Dataset/subs.csv')
file_path2 = os.path.join(path_dir, '../../1_Dataset/bollywood.csv')





# ==================================================
# Example 1
# Line Plot (Trend Visualization)
# ==================================================

# Definition (Interview Friendly)
# A line plot is used to show trends or changes in data
# over a sequence (usually time or ordered data).


subs = pd.read_csv(file_path1).squeeze('columns')

subs.plot()
plt.show()

# Explanation
# • Each value represents subscribers gained per day
# • Line plot helps visualize the growth trend





# ==================================================
# Example 2
# Bar Plot
# ==================================================

# Definition (Interview Friendly)
# A bar chart is used to compare categorical data.


movies = pd.read_csv(file_path2, index_col='movie').squeeze('columns')

num_movies = movies.value_counts()

num_movies.head(20).plot(kind='bar')
plt.show()

# Explanation
# • value_counts() counts movies done by each actor
# • head(20) selects top 20 actors
# • Bar chart compares number of movies per actor





# ==================================================
# Example 3
# Pie Chart
# ==================================================

# Definition (Interview Friendly)
# A pie chart shows the proportion or percentage
# contribution of categories.


num_movies.head(20).plot(kind='pie')
plt.show()

# Explanation
# • Shows percentage distribution of movies among top actors





# ==================================================
# Common Plot Types in Pandas
# ==================================================

# line  → Default line graph
# bar   → Bar chart
# pie   → Pie chart
# hist  → Histogram
# box   → Box plot
# area  → Area plot





# ==================================================
# Quick Revision
# ==================================================

# Series.plot() → used to create plots

# Important parameter
# kind = 'bar', 'pie', 'hist', etc.

# Example
# series.plot(kind='bar')

# plt.show() → displays the graph