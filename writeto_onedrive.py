
# df = ["hehe", "haha"]

# df.to_excel('3000new1.xlsx')

import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

#redirect_uri = 'https://onedrive.live.com/?authkey=%21ANwuwr2Xywtx%5FQ4&id=1D93133541FEA9C0%2112436&cid=1D93133541FEA9C0'
redirect_uri = 'http://localhost:8080/'
client_secret = 'PGD8Q~bE4WBt.RkZQpsLyVQj9G1XwZ5V29bB.cx3' #value
client_id='78907c8b-fe98-4f57-bcc6-1a9859d60515'
# api_base_url='https://api.onedrive.com/v1.0/'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

#client = onedrivesdk.get_default_client(client_id = client_id, scopes=scopes)
client = onedrivesdk.get_consumer_client(client_id= client_id, scopes=scopes)

# print("client: ", client)
auth_url = client.auth_provider.get_auth_url(redirect_uri)
# print("auth url: ", auth_url)
# #this will block until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
client.auth_provider.authenticate(code, redirect_uri, client_secret)
# Navigate One Drive
root_folder = client.item(drive='me', id='root').children.get()
for item in root_folder:
    if item.folder:
        print(item.name)
# id_of_file = root_folder[0].id
# print(id_of_file)
# client.item(drive='me', id='root').download('./Document.docx')
# client.item(drive='me', id=id_of_file).download('./Document.docx')

shared_items = client.item(id='985AF262A84C3FF2%21567').get()
# content = client.item(drive='me', id='985AF262A84C3FF2%21567').download('./SD.docx')
print(shared_items.name)
for item in shared_items:
   print(item)
