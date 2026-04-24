import seaborn as sns

# Load the built-in flights dataset
flights = sns.load_dataset("flights")

# Display the first 5 rows
print(flights.head())
#Rename Columns
flights.rename(
    columns={'passengers':'pass'},inplace=True)
print(flights.head())