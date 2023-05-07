#Preparing data for time series
def create_timeseries_data(df):
    import pandas as pd
    from writeto_onedrive import write_to_onedrive

    print("Fetching Triage Datetime")
    df = df[['TRIAGE_DATETIME']]
    df.columns = df.columns.str.title()

    write_to_onedrive(df, 'time_series_data.xlsx')
    # df.to_excel('C:\\Users\\Hp\\OneDrive\\FYP\\ts_data.xlsx')
    
import pandas as pd
from access_onedrive import create_onedrive_directdownload
new_data_onedrive_link = 'https://1drv.ms/x/s!AsCp_kE1E5Md6hQevRHs-ptqyPlE?e=Yizetg' #merged clean Data.xlsx
link = create_onedrive_directdownload(new_data_onedrive_link)
data = pd.read_excel(link) 
create_timeseries_data(data)
