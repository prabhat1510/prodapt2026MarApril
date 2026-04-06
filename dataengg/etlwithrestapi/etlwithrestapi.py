#Fetch data from API → transform → save
import requests
import pandas as pd

# EXTRACT
url = "https://jsonplaceholder.typicode.com/posts" #Public URL
response = requests.get(url,verify=False)
data = response.json()

df = pd.DataFrame(data)

# TRANSFORM
df = df[["userId", "id", "title"]]

# LOAD
df.to_csv("posts.csv", index=False)

print(df.head())