import requests

endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint, json={"query": "Hello World"})
# print(get_response.json())

get_response = requests.post(endpoint, json={"content": "Hello World 3"})
print(get_response.json())
