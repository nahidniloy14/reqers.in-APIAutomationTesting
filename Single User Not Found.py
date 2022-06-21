import requests
response3=requests.get("https://reqres.in/api/users/23")
print(response3.text)
print(response3.status_code)
assert response3.status_code == 404