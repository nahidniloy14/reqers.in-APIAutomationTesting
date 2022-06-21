import requests
response6=requests.get("https://reqres.in/api/unknown/23")
print(response6.text)
print(response6.status_code)
assert response6.status_code == 404
