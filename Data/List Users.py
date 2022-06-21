import requests
import configparser

from Payloads import listUsersPayload
from Utilities.configurations import *
from Utilities.Resources import *
url=getConfig()['API']['endpoint']+ApiResources.listUsers
response1=requests.get(url,params=listUsersPayload)

listUsers=response1.json()
print(listUsers)
