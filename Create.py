import requests
response7=requests.post("https://reqres.in/api/users",json=
{
    "name": "morpheus",
    "job": "leader",
    "id": "793",
    "createdAt": "2022-06-21T09:56:25.591Z"
}
)
print(response7.json())
assert response7.status_code == 201