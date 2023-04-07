import pandas as pd
from writeto_onedrive import write_to_onedrive

data_files = ['C:\\Users\\Hp\\OneDrive\\FYP\\cleaned_data_2019.xlsx', 'C:\\Users\\Hp\\OneDrive\\FYP\\cleaned_data_2020.xlsx', 'C:\\Users\\Hp\\OneDrive\\FYP\\cleaned_data_2021.xlsx']
# data_2019 = pd.read_excel('C:\\Users\\Hp\\OneDrive\\FYP\\cleaned_data_2019.xlsx')
# data_2020 = pd.read_excel('C:\\Users\\Hp\\OneDrive\\FYP\\cleaned_data_2020.xlsx')
# data_2021 = pd.read_excel('C:\\Users\\Hp\\OneDrive\\FYP\\cleaned_data_2021.xlsx')

list = []

for file in data_files:
    list.append(pd.read_excel(file))

merged_file = pd.DataFrame()

for file in list:
    merged_file = merged_file.append(file, ignore_index=True)
    
write_to_onedrive(merged_file)