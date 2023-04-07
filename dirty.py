import pandas as pd
from writeto_onedrive import write_to_onedrive

data = pd.read_excel('C:\\Users\\Hp\\OneDrive\\FYP\\Adult 2019 Anonymized.xlsx')

df = pd.DataFrame(data)
print(df.info())

# df.head(5)

"""DATA CLEANING"""

#dropping columns
df.pop(df.columns[0])
# df = df.drop(['A'], axis = 'columns')
# df = df.drop(['MR_DOB'], axis = 'columns')
# df = df.drop(['AJ'], axis = 'columns')

cols = ['A', 'MR_DOB', 'BP', 'TR_PULSE', 'TR_TEMP', 'TR_RESP', 'SYSTOLIC', 'DIASTOLIC', 'TEMPERATURE', 'WEIGHT', 'O2SAT', 'NURSE_USERID', 'NURSE_EMP_CODE', 'NURSE_NAME', 'DOCTOR_ID', 'DOCTOR_NAME', 'SPECIALTY', 'AJ', 'month', 'day', 'hour', 'lostriage', 'loshospital', 'losED', 'new_mr']
for col_name in cols:
    df = df.drop([col_name], axis = 'columns')
    
print("Columns dropped")
print(df.info())
