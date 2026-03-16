import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
print("-------------")
#Dictionary
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
print("------Write Data to CSV file-------")
data = [
    ["id", "name", "salary"],
    [1, "John", 50000],
    [2, "Alice", 60000]
]
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
