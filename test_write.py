# requirements
import requests
import json
import urllib
import os
from getpass import getpass
import time
from datetime import datetime

URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
client_id = "78907c8b-fe98-4f57-bcc6-1a9859d60515"
permissions = ['files.readwrite']
response_type = 'token'
#redirect_uri = 'https://onedrive.live.com/?authkey=%21ANwuwr2Xywtx%5FQ4&id=1D93133541FEA9C0%2112436&cid=1D93133541FEA9C0'
redirect_uri = 'http://localhost:8080/'
scope = ''
for items in range(len(permissions)):
    scope = scope + permissions[items]
    if items < len(permissions)-1:
        scope = scope + '+'

print('Click over this link ' +URL + '?client_id=' + client_id + '&scope=' + scope + '&response_type=' + response_type+\
     '&redirect_uri=' + urllib.parse.quote(redirect_uri))
print('Sign in to your account, copy the whole redirected URL.')
code = input("Paste the URL here :")
token = code[(code.find('access_token') + len('access_token') + 1) : (code.find('&token_type'))]
URL = 'https://graph.microsoft.com/v1.0/'
HEADERS = {'Authorization': 'Bearer ' + token}
response = requests.get(URL + 'me/drive', headers = HEADERS)
print(response)
if (response.status_code == 200):
    response = json.loads(response.text)
    print('Connected to the OneDrive of', response['owner']['user']['displayName']+' (',response['driveType']+' ).', \
         '\nConnection valid for one hour. Reauthenticate if required.')
elif (response.status_code == 401):
    response = json.loads(response.text)
    print('API Error! : ', response['error']['code'],\
         '\nSee response for more details.')
else:
    response = json.loads(response.text)
    print('Unknown error! See response for more details.')

print(response)