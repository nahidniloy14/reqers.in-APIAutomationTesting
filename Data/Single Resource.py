import requests
response5=requests.get("https://reqres.in/api/unknown/2",params=
{
    "data": {
        "id": 2,
        "name": "fuchsia rose",
        "year": 2001,
        "color": "#C74375",
        "pantone_value": "17-2031"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
)
listResource=response5.json()
print(listResource)
print(response5.status_code)
assert response5.status_code == 200
