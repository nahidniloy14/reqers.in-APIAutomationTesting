import requests
response14=requests.get("https://reqres.in/api/users?delay=3")
print(response14.json())
print(response14.status_code)
assert response14.status_code == 200
