#Data Transformation Example
#Example: Increase salary by 10% while converting CSV → JSON

import csv
import json

result = []

with open("employees.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        salary = int(row["salary"])
        row["salary"] = salary * 1.10
        result.append(row)

with open("updated_employees.json","w") as file:
    json.dump(result,file,indent=4)
