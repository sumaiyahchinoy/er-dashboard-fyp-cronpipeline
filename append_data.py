
def append_all_data():
    import pandas as pd
    from access_onedrive import create_onedrive_directdownload
    import writeto_onedrive
    import importlib
    importlib.reload(writeto_onedrive)
    from writeto_onedrive import write_to_onedrive
    
    data_files = ['https://1drv.ms/x/s!AsCp_kE1E5Md510L7cgZfxy_ifCq?e=bNj2eY', 'https://1drv.ms/x/s!AsCp_kE1E5Md6TUUuL5DtjrFTggO?e=xA3jaE', 'https://1drv.ms/x/s!AsCp_kE1E5Md6TSDbgcW_MFQzySB?e=oWsFUm']

    data = pd.DataFrame()
    for file in range(len(data_files)):
        data = pd.concat([data, pd.read_excel(create_onedrive_directdownload(data_files[file]))])

    write_to_onedrive(data, "merged_data.xlsx")


def append_new_data(df):
    import pandas as pd
    from access_onedrive import create_onedrive_directdownload
    import writeto_onedrive
    import importlib
    importlib.reload(writeto_onedrive)
    from writeto_onedrive import write_to_onedrive
    
    new_data = df

    old_data_link = 'https://1drv.ms/x/s!AsCp_kE1E5Md6hQevRHs-ptqyPlE?e=5gBagY' #merged data.xlsx
    old_data_od_link = create_onedrive_directdownload(old_data_link)
    old_data = pd.read_excel(old_data_od_link)

    final_data = pd.concat([old_data, new_data])
    
    write_to_onedrive(final_data, "merged_clean_data.xlsx")
    print("New data appended successfully.")
    
    from ts_data import create_timeseries_data