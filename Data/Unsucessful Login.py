import requests
response13=requests.post("https://reqres.in/api/register",json=
{
    "email": "peter@klaven"
}
)
print(response13.json())
assert response13.status_code == 400
