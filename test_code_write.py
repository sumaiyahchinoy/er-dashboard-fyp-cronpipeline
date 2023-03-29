# requirements
import requests
import json
import urllib
import os
from getpass import getpass
import time
from datetime import datetime

# Get code
URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
client_id = "78907c8b-fe98-4f57-bcc6-1a9859d60515"
permissions = ['offline_access', 'files.readwrite', 'User.Read']
response_type = 'code'
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
code = code[(code.find('?code') + len('?code') + 1) :]

URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

response = requests.post(URL + '?client_id=' + client_id + '&scope=' + scope + '&grant_type=authorization_code' +\
     '&redirect_uri=' + urllib.parse.quote(redirect_uri)+ '&code=' + code)

print(response)