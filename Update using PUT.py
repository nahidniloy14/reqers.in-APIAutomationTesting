import requests
response8=requests.put("https://reqres.in/api/users/2",data=
{
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": "2022-06-21T10:01:04.391Z"
}
)
print(response8.json())
assert response8.status_code == 200