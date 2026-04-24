import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("D:/Cloud Learning/ML-For-Beginners/5-Clustering/data/nigerian-songs.csv")
print(df.head())
print(df.info())#information about dataframe
print(df.isnull().sum())#check for null values
print("********************************************************************")
#Look at the general values of the data. Note that popularity can be '0' - and there are many rows with that value
print(df.describe())
print("********************************************************************")
#Let's look at the distribution of popularity
#plt.hist(df["popularity"])
#plt.show()
#Let's examine the genres. 
#Quite a few are listed as 'Missing' which means they aren't categorized in the dataset with a genre 

top = df['artist_top_genre'].value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x=top[:5].index,y=top[:5].values)
plt.xticks(rotation=45)
plt.title('Top genres',color = 'blue')
#plt.show()

#Remove 'Missing' genres, as it's not classified in Spotify
df = df[df['artist_top_genre'] != 'Missing']
top = df['artist_top_genre'].value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x=top.index,y=top.values)
plt.xticks(rotation=45)
plt.title('Top genres',color = 'blue')
#plt.show()
#The top three genres comprise the greatest part of the dataset, so let's focus on those
df = df[(df['artist_top_genre'] == 'afro dancehall') | (df['artist_top_genre'] == 'afropop') | (df['artist_top_genre'] == 'nigerian pop')]
df = df[(df['popularity'] > 0)]
top = df['artist_top_genre'].value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x=top.index,y=top.values)
plt.xticks(rotation=45)
plt.title('Top genres',color = 'blue')
#plt.show()
'''
The data is not strongly correlated except between energy and loudness, 
which makes sense. Popularity has a correspondence to release data, 
which also makes sense, as more recent songs are probably more popular. 
Length and energy seem to have a correlation - perhaps shorter songs are 
more energetic?
'''
corrmat = df.corr(numeric_only=True)
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)
#plt.show()

'''
Are the genres significantly different in the perception of their danceability, 
based on their popularity? Examine our top three genres data distribution 
for popularity and danceability along a given x and y axis 
'''

sns.set_theme(style="ticks")

# Show the joint distribution using kernel density estimation
g = sns.jointplot(
    data=df,
    x="popularity", y="danceability", hue="artist_top_genre",
    kind="kde",
)
#plt.show()
'''
In general, the three genres align in terms of their popularity and danceability.  
A scatterplot of the same axes shows a similar pattern of convergence. Try a 
scatterplot to check the distribution of data per genre
'''
sns.FacetGrid(df, hue="artist_top_genre", size=5) \
   .map(plt.scatter, "popularity", "danceability") \
   .add_legend()
plt.show()
'''
Let's try to cluster the data using the KMeans algorithm. We'll use the 
danceability and popularity columns to cluster the data. We'll use the 
Elbow method to determine the optimal number of clusters.

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#Standardize the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['popularity', 'danceability']])

#Elbow method
inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow method')
plt.show()'''