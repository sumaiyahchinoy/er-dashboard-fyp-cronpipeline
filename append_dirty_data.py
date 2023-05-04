import pandas as pd
from access_onedrive import create_onedrive_directdownload
   
data_files = ['https://1drv.ms/x/s!AsCp_kE1E5Md510L7cgZfxy_ifCq?e=bNj2eY', 'https://1drv.ms/x/s!AsCp_kE1E5Md6TUUuL5DtjrFTggO?e=xA3jaE', 'https://1drv.ms/x/s!AsCp_kE1E5Md6TSDbgcW_MFQzySB?e=oWsFUm']
# print(data_files[1])
# print(len(data_files))

# file_link = pd.DataFrame()
file_link = []
for file in range(len(data_files)):
    print(file)
    file_link.append(create_onedrive_directdownload(data_files[file]))
print(file_link)

# data = pd.DataFrame()
# for file in data_files:
#     data.append(pd.read_excel(create_onedrive_directdownload(file)))

# data = pd.read_excel(link)

# df = df_diagnosis.append(df_null)
# df = df.sort_index()
    