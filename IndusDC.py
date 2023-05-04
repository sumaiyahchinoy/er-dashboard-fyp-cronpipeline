def clean_data():
    #LIBRARIES
    import pandas as pd
    from access_onedrive import create_onedrive_directdownload
    # from writeto_onedrive import write_to_onedrive
    from MedicalNER import medner

    # data = pd.read_excel('C:\\Users\\Hp\\OneDrive\\FYP\\Adult 2021 Anonymized.xlsx') ##must change the reading location to merged file
    onedrive_link = 'https://1drv.ms/x/s!AsCp_kE1E5Md6UkKXCAorwdeI3bi?e=PfM5DJ' #pass actual dirty merged file
    link = create_onedrive_directdownload(onedrive_link)
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
    df = df[df.Triage_Datetime != df.ER_No]
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
    
    medner(new_df)
    # write_to_onedrive(new_df) #add write to one drive in med ner
    
clean_data()