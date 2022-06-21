import requests
response10=requests.post("https://reqres.in/api/register",json=
{
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
)
print(response10.json())
assert response10.status_code == 200
