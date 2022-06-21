import requests
response8=requests.patch("https://reqres.in/api/users/2",data=
{
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": "2022-06-21T10:03:36.302Z"
}
)
print(response8.json())
assert response8.status_code == 200