#JSON to CSV
import json
import csv

with open("employees.json") as json_file:
    data = json.load(json_file)

print("**************************")
print(data)
print(data[0])
print(data[0].keys())
print("**************************")
with open("employees1.csv","w",newline="") as csv_file:

    headers = data[0].keys()

    writer = csv.DictWriter(csv_file, fieldnames=headers)

    writer.writeheader()
    writer.writerows(data)

print("JSON converted to CSV successfully")
