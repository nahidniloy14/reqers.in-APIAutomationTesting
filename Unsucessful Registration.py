import requests
response11=requests.post("https://reqres.in/api/register",json=
{
    "email": "sydney@fife"
}
)
print(response11.json())
assert response11.status_code == 400
