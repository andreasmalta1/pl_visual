import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
password = getpass()

# data = {"title": "This is the title"}
auth_response = requests.post(
    endpoint, json={"username": "andreas", "password": "1234"}
)

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    print(token)
    headers = {"Authorization": f"Bearer {token}"}
    print(headers)

    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
