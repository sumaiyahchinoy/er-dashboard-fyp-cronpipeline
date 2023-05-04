def write_to_onedrive(df, file_name):
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
    fyp_folder_id =""
    for item in root_folder:
        if item.folder:
            # print(item.id + " " + item.name)
            if (item.name == "FYP"):
                fyp_folder_id = item.id
                print(item.name)

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
    print("Conversion Succesful")
    # # print(file)
    # # returned_item = client.item(id='1D93133541FEA9C0!12436').children['newfile.txt'].upload(file)   
    # returned_item = client.item(id=fyp_folder_id).children['cleaned_dataset_merged.xlsx'].upload('test.xlsx')
    returned_item = client.item(id=fyp_folder_id).children[file_name].upload('test.xlsx')  
    returned_item
    print("File successfully uploaded")
    # returned_item
