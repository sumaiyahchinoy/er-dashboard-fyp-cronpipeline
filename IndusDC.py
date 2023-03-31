    # -*- coding: utf-8 -*-

def clean_data():
    #LIBRARIES
    import pandas as pd

    #Configurations
    pd.set_option("display.max_rows", None)



    data = pd.read_excel('C:\\Users\\Hp\\OneDrive\\FYP\\Adult 2019 Anonymized.xlsx')

    """# New section"""

    df = pd.DataFrame(data)
    # df.info()

    # df.head(5)

    """DATA CLEANING"""

    df.pop(df.columns[0])
    df = df.drop(['A'], axis = 'columns')
    df = df.drop(['MR_DOB'], axis = 'columns')
    df = df.drop(['AJ'], axis = 'columns')

    #Dropping columns with ALL null values
    df.dropna(how = 'all', axis= 1)

    # df.info()

    """DATA MANIPULATION"""

    df['AGE_YEARS'] = df['AGE_YEARS'].round(decimals=0).astype(int)

    #Changing column values to Camel Casing
    df['CITY'] = df['CITY'].str.title()
    #df['CITY']
    df['AREA'] = df['AREA'].str.title()
    #df['AREA']
    # df.tail(5)

    #Grouping Values in the Area column
    # df['AREA'].sort_values().value_counts()

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
    # print(df.head(5))

    #Nurse Employee Codes with invalid user name
    df.loc[(df['NURSE_EMP_CODE'] == 'Invalid User Name...........'), 'NURSE_EMP_CODE'] = 'Unidentified'
    # print(df['NURSE_EMP_CODE'].value_counts())

    df['NURSE_NAME'] = df['NURSE_NAME'].str.title()
    # print(df['NURSE_NAME'].describe)

    # print(df['DISPOSITION'].value_counts()) #no change
    #df['DISPOSITION'].describe

    df['HOPI_'] = df['HOPI_'].str.title()

    # print(df['HOPI_'])

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
    #print(df['ED_DX'].value_counts())
    # print(df['ED_DX'])

    df['DOCTOR_NAME'] = df['DOCTOR_NAME'].str.title()
    df['SPECIALTY'] = df['SPECIALTY'].str.title()

    # print(df['ADMISSION_WARD'].value_counts())
    # print(df['DISCHARGE_WARD'].value_counts())

    # print(df['loshospital'].value_counts())

    #CHANGING COLUMN NAMES
    #df.info()
    new_df = pd.DataFrame(df)
    new_df.columns = new_df.columns.str.title()

    new_df.columns = new_df.columns.str.replace("Er_No", "ER_No")
    new_df.columns = new_df.columns.str.replace("Bp", "BP")
    new_df.columns = new_df.columns.str.replace("Tr_Pulse", "Triage_Pulse")
    new_df.columns = new_df.columns.str.replace("Tr_Temp", "Triage_Temp")
    new_df.columns = new_df.columns.str.replace("Tr_Pulse", "Triage_Pulse")
    new_df.columns = new_df.columns.str.replace("O2Sat", "O2_Saturation")
    new_df.columns = new_df.columns.str.replace("Nurse_Userid", "Nurse_User_ID")
    new_df.columns = new_df.columns.str.replace("Hopi_", "HOPI")
    new_df.columns = new_df.columns.str.replace("Er_Dx", "ER_Diagnosis")
    new_df.columns = new_df.columns.str.replace("Doctor_Id", "Doctor_ID")
    new_df.columns = new_df.columns.str.replace("Lostriage", "Los_Triage")
    new_df.columns = new_df.columns.str.replace("Losed", "Los_ED")
    new_df.columns = new_df.columns.str.replace("Loshospital", "Los_Hospital")
    new_df.columns = new_df.columns.str.replace("New_Mr", "New_MR")
    new_df.columns = new_df.columns.str.replace("Triagecomplaint", "Triage_Complaint")
    # new_df.info()

    #Changing Data Types 
    new_df['ER_No'] = new_df['ER_No'].astype('str')

    #new_df.info()
    # new_df['Admission_Date'].value_counts()

    print("Cleaning was successful")
    df.to_excel('indus clean 2.xlsx')
    
clean_data()