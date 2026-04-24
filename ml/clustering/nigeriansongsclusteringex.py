import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("D:/Cloud Learning/ML-For-Beginners/5-Clustering/data/nigerian-songs.csv")
print(df.head())
#We will focus only on 3 genres. Maybe we can get 3 clusters built!
df = df[(df['artist_top_genre'] == 'afro dancehall') | (df['artist_top_genre'] == 'afropop') | (df['artist_top_genre'] == 'nigerian pop')]
df = df[(df['popularity'] > 0)]
top = df['artist_top_genre'].value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x=top.index,y=top.values)
plt.xticks(rotation=45)
plt.title('Top genres',color = 'blue')
plt.show()
print(df.head())

'''
How clean is this data? Check for outliers using box plots. 
We will concentrate on columns with fewer outliers (although you could clean out the outliers). 
Boxplots can show the range of the data and will help choose which columns to use. 
Note, Boxplots do not show variance, an important element of good clusterable data 
(https://stats.stackexchange.com/questions/91536/deduce-variance-from-boxplot)
'''
plt.figure(figsize=(20,20), dpi=200)

plt.subplot(4,3,1)
sns.boxplot(x = 'popularity', data = df)

plt.subplot(4,3,2)
sns.boxplot(x = 'acousticness', data = df)

plt.subplot(4,3,3)
sns.boxplot(x = 'energy', data = df)

plt.subplot(4,3,4)
sns.boxplot(x = 'instrumentalness', data = df)

plt.subplot(4,3,5)
sns.boxplot(x = 'liveness', data = df)

plt.subplot(4,3,6)
sns.boxplot(x = 'loudness', data = df)

plt.subplot(4,3,7)
sns.boxplot(x = 'speechiness', data = df)

plt.subplot(4,3,8)
sns.boxplot(x = 'tempo', data = df)

plt.subplot(4,3,9)
sns.boxplot(x = 'time_signature', data = df)

plt.subplot(4,3,10)
sns.boxplot(x = 'danceability', data = df)

plt.subplot(4,3,11)
sns.boxplot(x = 'length', data = df)

plt.subplot(4,3,12)
sns.boxplot(x = 'release_date', data = df)
plt.show()
'''
Choose several columns with similar ranges. Make sure to include the artist_top_genre 
column to keep our genres straight. 
'''
from sklearn.preprocessing import LabelEncoder, StandardScaler
le = LabelEncoder()

# scaler = StandardScaler()

X = df.loc[:, ('artist_top_genre','popularity','danceability','acousticness','loudness','energy')]

y = df['artist_top_genre']

X['artist_top_genre'] = le.fit_transform(X['artist_top_genre'])

# X = scaler.fit_transform(X)

y = le.transform(y)

'''
K-Means Clustering has the drawback of needing to tell it how many clusters to build. 
We know there are three song types, so let's focus on 3.
'''

from sklearn.cluster import KMeans

nclusters = 3 
seed = 0

km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X)

# Predict the cluster for each data point

y_cluster_kmeans = km.predict(X)
print(y_cluster_kmeans)

df['cluster'] = y_cluster_kmeans

#Let's visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='popularity', y='danceability', hue='cluster', palette='viridis', s=100)

# Plot the centroids
centroids_x = km.cluster_centers_[:, 1]  # 'popularity' is at index 1 in training data X
centroids_y = km.cluster_centers_[:, 2]  # 'danceability' is at index 2 in training data X
plt.scatter(centroids_x, centroids_y, s=300, c='red', marker='X', label='Centroids')

from matplotlib.patches import Ellipse

# Draw enclosed areas (ellipses) for each cluster
palette = sns.color_palette('viridis', nclusters)
for i in range(nclusters):
    points_x = df[df['cluster'] == i]['popularity']
    points_y = df[df['cluster'] == i]['danceability']
    if len(points_x) > 0:
        # Since 'popularity' and 'danceability' have very different scales, a regular Circle
        # would distort the axes. We use an Ellipse scaled to the max distance in each respective axis.
        max_dist_x = np.max(np.abs(points_x - centroids_x[i]))
        max_dist_y = np.max(np.abs(points_y - centroids_y[i]))
        
        # Multiply by 2 because width/height are the full bounding box dimension, and add a small buffer (e.g., 2.1)
        ellipse = Ellipse((centroids_x[i], centroids_y[i]), width=max_dist_x * 2.1, height=max_dist_y * 2.1, color=palette[i], alpha=0.15)
        plt.gca().add_patch(ellipse)

plt.title('K-Means Clustering of Nigerian Songs')
plt.xlabel('Popularity')
plt.ylabel('Danceability')
plt.legend(title='Cluster')
plt.show()
#Those numbers don't mean much to us, so let's get a 'silhouette score' 
# to see the accuracy. Our score is in the middle.
from sklearn import metrics
score = metrics.silhouette_score(X, y_cluster_kmeans)
print(score)


#Looks like 3 is a good number after all. Fit the model again and create a scatterplot of your clusters. 
#They do group in bunches, but they are pretty close together.
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3)
kmeans.fit(X)
labels = kmeans.predict(X)
plt.scatter(df['popularity'],df['danceability'],c = labels)
plt.xlabel('popularity')
plt.ylabel('danceability')
plt.show()
'''
This model's accuracy is not bad, but not great. It may be that the data may not lend itself well 
to K-Means Clustering. You might try a different method.
'''
labels = kmeans.labels_

correct_labels = sum(y == labels)

print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))

print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))

from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(x=range(1, 11), y=wcss, marker='o', color='red')
plt.title('Elbow')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()