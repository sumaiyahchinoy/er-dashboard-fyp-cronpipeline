def write_to_onedrive(df, file_name):
    import onedrivesdk
    from onedrivesdk.helpers import GetAuthCodeServer

    print("File name = ", file_name)
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
    fyp_folder_id =""
    for item in root_folder:
        if item.folder:
            # print(item.id + " " + item.name)
            if (item.name == "FYP"):
                fyp_folder_id = item.id
                print("Folder Name = ", item.name)

    # shared_items = client.item(id='985AF262A84C3FF2%21567').get()
    # print(shared_items.name)
    # for item in shared_items:
    #    print(item)

    # fyp_folder = client.item(id='1D93133541FEA9C0!12436').children.get()
    # print(fyp_folder.name)
    # for item in fyp_folder:
    #    print(item.name)

    # import pandas as pd
    # df = pd.DataFrame(["heheeh", "huuh"])
    print("Converting Dataframe to Excel File")
    df.to_excel('test.xlsx')
    print("Conversion Successful")
    # # print(file)
    # # returned_item = client.item(id='1D93133541FEA9C0!12436').children['newfile.txt'].upload(file)   
    # returned_item = client.item(id=fyp_folder_id).children['cleaned_dataset_merged.xlsx'].upload('test.xlsx')
    # import os
    # with open('test.xlsx', 'rb') as file:
    #     returned_item = client.item(id=fyp_folder_id).children[file_name].upload(file)  
    returned_item = client.item(id=fyp_folder_id).children[file_name].upload('test.xlsx')  
    returned_item
    print("File successfully uploaded")
    # returned_item


def session_write_to_onedrive(df, file_name):
    from onedrivesdk.helpers import GetAuthCodeServer
    from onedrivesdk.session import Session
    from onedrivesdk import OneDriveClient
    import os

    print("File name = ", file_name)
    
    redirect_uri = 'http://localhost:8080/'
    client_secret = 'PGD8Q~bE4WBt.RkZQpsLyVQj9G1XwZ5V29bB.cx3' #value
    client_id='78907c8b-fe98-4f57-bcc6-1a9859d60515'
    # api_base_url='https://api.onedrive.com/v1.0/'
    
    scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
    session = Session(redirect_uri=redirect_uri, client_id=client_id, scope=scopes)


    #client = onedrivesdk.get_default_client(client_id = client_id, scopes=scopes)
    # client = onedrivesdk.get_consumer_client(client_id= client_id, scopes=scopes)
    client = OneDriveClient.from_session(session)
    # print("client: ", client)
    # auth_url = client.auth_provider.get_auth_url(redirect_uri)
    auth_url = client.auth_provider.get_auth_url(redirect_uri=redirect_uri)
    # print("auth url: ", auth_url)
    # #this will block until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    # Navigate One Drive
    root_folder = client.item(drive='me', id='root').children.get()
    fyp_folder_id =""
    for item in root_folder:
        if item.folder:
            # print(item.id + " " + item.name)
            if (item.name == "FYP"):
                fyp_folder_id = item.id
                print("Folder Name = ", item.name)


    print("Converting Dataframe to Excel File")
    df.to_excel('test.xlsx')
    print("Conversion Successful")
    
    file_path = 'test.xlsx'
    chunk_size = 10 * 1024 * 1024  # 10 MB
    file_size = os.path.getsize(file_path)
    
    upload_session = client.item(id=fyp_folder_id).children[file_name].create_upload_session({'@name.conflictBehavior': 'rename'}).initiate_upload_session(file_size)
  
    # with open('test.xlsx', 'rb') as file:
    #     returned_item = client.item(id=fyp_folder_id).children[file_name].upload(file)  
    # returned_item = client.item(id=fyp_folder_id).children[file_name].upload('test.xlsx')  
    # returned_item
    
    with open(file_path, 'rb') as file:
        while not upload_session.completed:
            chunk = file.read(chunk_size)
            upload_session.upload_range(chunk)
            print(f"Uploaded {upload_session.bytes_transferred} bytes of {file_size}")

# Commit the upload
    upload_result = upload_session.finish_upload_session()
    upload_result
    print("File successfully uploaded")
    # returned_item
    
    
def session_write(df, file_name):
    import onedrivesdk
    from onedrivesdk.helpers import GetAuthCodeServer

    print("File name = ", file_name)
    
    redirect_uri = 'http://localhost:8080/'
    client_secret = 'PGD8Q~bE4WBt.RkZQpsLyVQj9G1XwZ5V29bB.cx3' #value
    client_id='78907c8b-fe98-4f57-bcc6-1a9859d60515'
    scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
    
    client = onedrivesdk.get_consumer_client(client_id= client_id, scopes=scopes)
    
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    # #this will block until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    
    # Navigate One Drive
    root_folder = client.item(drive='me', id='root').children.get()
    fyp_folder_id =""
    for item in root_folder:
        if item.folder:
            # print(item.id + " " + item.name)
            if (item.name == "FYP"):
                fyp_folder_id = item.id
                print("Folder Name = ", item.name)

    print("Converting Dataframe to Excel File")
    df.to_excel('test.xlsx')
    print("Conversion Successful")

    returned_item = client.item(id=fyp_folder_id).children[file_name].upload('test.xlsx', chunk_size = 1024*1024*10, conflict_behavior = 'rename')  
    returned_item
    print("File successfully uploaded")
    # returned_item

import pandas as pd

from access_onedrive import create_onedrive_directdownload

link = create_onedrive_directdownload("https://1drv.ms/x/s!AsCp_kE1E5Md6U4PwNcWkXp_SnEL?e=FQNmYU")
new_df = pd.read_excel(link)
df = pd.DataFrame(new_df) 
print(type(df))

session_write(df, "new.xlsx")