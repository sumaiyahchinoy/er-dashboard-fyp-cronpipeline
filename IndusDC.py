def clean_data():
    #LIBRARIES
    import pandas as pd
    from access_onedrive import create_onedrive_directdownload
    from MedicalNER import medner

    new_data_onedrive_link = 'https://1drv.ms/x/s!AsCp_kE1E5Md6hHi2av2ez6BdQ9S?e=UexbnL' #New Data.xlsx
    link = create_onedrive_directdownload(new_data_onedrive_link)
    data = pd.read_excel(link)    
    
    #Convert Excel to DataFrame
    df = pd.DataFrame(data)

    """DATA CLEANING"""

    #dropping columns
    df.pop(df.columns[0])

    cols = ['A', 'MR_DOB', 'BP', 'TR_PULSE', 'TR_TEMP', 'TR_RESP', 'SYSTOLIC', 'DIASTOLIC', 'TEMPERATURE', 'WEIGHT', 'O2SAT', 'NURSE_USERID', 'NURSE_EMP_CODE', 'DOCTOR_ID', 'month', 'day', 'hour', 'lostriage', 'loshospital', 'losED', 'new_mr']
    for col_name in cols:
        df = df.drop([col_name], axis = 'columns')

    #Dropping columns with ALL null values
    df.dropna(how = 'all', axis= 1)
    
    #dropping records
    # df = df[df.TRIAGE_DATETIME != df.ER_NO]
    df.drop(df[df['SPECIALTY'] == "GYNAE & OBS"].index, inplace = True)

    """DATA MANIPULATION"""

    df['AGE_YEARS'] = df['AGE_YEARS'].round(decimals=0).astype(int)

    #Changing column values to Camel Casing
    df['CITY'] = df['CITY'].str.title()
    df['AREA'] = df['AREA'].str.title()

    #Grouping Values in the Area column
    df.loc[(df['AREA'] == '-') | (df['AREA'] == '.') | (df['AREA'] == '----') | (df['AREA'] == '--') | (df['AREA'] == '---'), 'AREA'] = 'Unspecified'
    df.loc[(df['AREA'] == 'Defence Housing Authority') | (df['AREA'] == '.'), 'AREA'] = 'Defence'
    df.loc[(df['AREA'] == 'Bhitai Colony')] = 'Bhittai Colony'
    df.loc[(df['AREA'] == 'Gulshan Street')] = 'Gulshan-E-Iqbal'
    df.loc[(df['AREA'] == 'Malir Cant') | (df['AREA'] == 'Cant'), 'AREA'] = 'Malir Cantt'
    df.loc[(df['AREA'] == 'Cant Road')] = 'Cantt Road'
    df.loc[(df['AREA'] == 'Corossing')] = 'Crossing'
    df.loc[(df['AREA'] == 'Ghribabad Market')] = 'Ghareebabad'
    df.loc[(df['AREA'] == 'Khndyaro')] = 'Kandiaro'
    df.loc[(df['AREA'] == 'Dawood Churangi')] = 'Dawood Chowrangi'
    df.loc[(df['AREA'] == 'Steel Mil')] = 'Steel Mill'
    df.loc[(df['AREA'] == 'Landhi Town')] = 'Landhi'
    df.loc[(df['AREA'] == 'Saudaabad')] = 'Saudabad'
    df.loc[(df['AREA'] == 'Satalite Town')] = 'Satellite Town'
    df.loc[(df['AREA'] == 'Haidri')] = 'Hyderi'
    df.loc[(df['AREA'] == 'Islam Abad')] = 'Islamabad'
    df.loc[(df['AREA'] == 'Gulshan-e-Mamar')] = 'Gulshan-e-Maymar'
    df.loc[(df['AREA'] == 'Site Area') | (df['AREA'] == 'S.I.T.E Area')] = 'SITE'
    df.loc[(df['AREA'] == 'P I D C')] = 'PIDC'

    #Preparing Triage Complaint Column
    df['TRIAGECOMPLAINT'] = df['TRIAGECOMPLAINT'].str.title()
    complaints = df['TRIAGECOMPLAINT'] .str.split(",", n = -1, expand = True)
    #print(complaints.tail(10))
    df['TRIAGECOMPLAINT_1'] = complaints[0]
    df['TRIAGECOMPLAINT_2'] = complaints[1]
    df['TRIAGECOMPLAINT_3'] = complaints[2]
    df['TRIAGECOMPLAINT_4'] = complaints[3]
    df['TRIAGECOMPLAINT_5'] = complaints[4]
    df = df.drop(['TRIAGECOMPLAINT'], axis = "columns")

    df['HOPI_'] = df['HOPI_'].str.title()

    df['ED_DX'] = df['ED_DX'].str.title()
    df.loc[(df['ED_DX'] == 'Rta'), 'ED_DX'] = 'RTA'
    df.loc[(df['ED_DX'] == 'Uti'), 'ED_DX'] = 'UTI'
    df.loc[(df['ED_DX'] == 'Apd'), 'ED_DX'] = 'APD'
    df['ED_DX'] = df['ED_DX'].str.replace('Uti','UTI', regex = True)
    df['ED_DX'] = df['ED_DX'].str.replace('Apd','APD', regex = True)
    df['ED_DX'] = df['ED_DX'].str.replace(' + ',', ', regex = True)
    df['ED_DX'] = df['ED_DX'].str.replace('+',', ', regex = True)
    df['ED_DX'] = df['ED_DX'].str.replace('?','', regex = True)
    df['ED_DX'] = df['ED_DX'].str.replace('//',', ', regex = True)
    df['ED_DX'] = df['ED_DX'].str.replace(',,',', ', regex = True)
    df['ED_DX'] = df['ED_DX'].str.replace('>','', regex = True)

    df = df.drop_duplicates(subset=['ER_No', 'Gender', 'City', 'Area', 'Age_Years', 'Triage_Datetime', 'Acuity', 'Visit_Datetime', 'Nurse_Name', 'Disposition', 'Disposition_Time', 'HOPI', 'Ed_Dx', 'Doctor_Name', 'Specialty', 'Admission_Date', 'Admission_Ward', 'Discharge_Ward', 'Discharge_Datetime', 'Aj', 'Shift', 'New_Doctor_Name', 'New_Nurse_Name', 'Triage_Complaint_1', 'Triage_Complaint_2', 'Triage_Complaint_3', 'Triage_Complaint_4', 'Triage_Complaint_5'], inplace=False, ignore_index=False)
    #CHANGING COLUMN NAMES
    #df.info()
    new_df = pd.DataFrame(df)
    new_df.columns = new_df.columns.str.title()

    new_df.columns = new_df.columns.str.replace("Er_No", "ER_No")
    new_df.columns = new_df.columns.str.replace("Hopi_", "HOPI")
    new_df.columns = new_df.columns.str.replace("Er_Dx", "ER_Diagnosis")
    new_df.columns = new_df.columns.str.replace("Triagecomplaint", "Triage_Complaint")

    #Changing Data Types 
    new_df['ER_No'] = new_df['ER_No'].astype('str')

    print("Cleaning was successful")
    # df.to_excel('indus clean 2.xlsx')
    
    from ts_data import create_timeseries_data
    create_timeseries_data(new_df)
    print("Created Data for Time Series")
    
    print("Performing Medical NER")
    medner(new_df)
    print("Medical NER Performed")
    # write_to_onedrive(new_df) #add write to one drive in med ner
    
# clean_data()