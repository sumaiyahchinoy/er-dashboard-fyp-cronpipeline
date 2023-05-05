def write_to_onedrive(df, file_name):
    import onedrivesdk
    from onedrivesdk.helpers import GetAuthCodeServer

    print("File name = ", file_name)

    redirect_uri = 'http://localhost:8080/'
    client_secret = 'PGD8Q~bE4WBt.RkZQpsLyVQj9G1XwZ5V29bB.cx3' #value
    client_id='78907c8b-fe98-4f57-bcc6-1a9859d60515'
    scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

    client = onedrivesdk.get_consumer_client(client_id= client_id, scopes=scopes)
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    #this will block until we have the code
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

    #returned_item = client.item(id=fyp_folder_id).children[file_name].upload(file)  
    returned_item = client.item(id=fyp_folder_id).children[file_name].upload_async('test.xlsx')  
    returned_item
    print("File successfully uploaded")

