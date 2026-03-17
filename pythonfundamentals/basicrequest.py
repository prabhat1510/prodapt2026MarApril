import requests

#response = requests.get("https://jsonplaceholder.typicode.com/users")
response = requests.get("http://127.0.0.1:8000/about")
print(response.status_code)
print(response.json())
