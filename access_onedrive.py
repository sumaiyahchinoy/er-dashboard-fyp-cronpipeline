import base64
import pandas as pd
#Convert OneDrive URL to Direct Download URL which conforms to OneDrive API
def create_onedrive_directdownload (onedrive_link):
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
    resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
    return resultUrl

# onedrive_link = "https://1drv.ms/x/s!AsCp_kE1E5Md52GlJNVCZuIy8qE6?e=jsP34P"
# link = create_onedrive_directdownload(onedrive_link)
# print(link)

# df = pd.read_excel(link)
# print(df.head())