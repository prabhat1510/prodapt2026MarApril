import csv
import json

csv_file = "employees.csv"
json_file = "employees.json"

data = []

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append(row)

print(data)
with open(json_file, "w") as file:
    json.dump(data, file, indent=4)

print("CSV converted to JSON successfully")
