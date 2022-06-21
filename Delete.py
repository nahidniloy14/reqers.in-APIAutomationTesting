import requests
response9=requests.delete("https://reqres.in/api/users/2")
print(response9.status_code)
assert response9.status_code == 204