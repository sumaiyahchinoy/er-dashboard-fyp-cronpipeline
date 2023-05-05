#Preparing data for time series
def create_timeseries_data():
    import pandas as pd

    data = pd.read_excel('C:\\Users\\Hp\\OneDrive\\FYP\\merged_data_final.xlsx')

    print("Converting to data frame")
    df = pd.DataFrame(data)

    print("Fetching selected columns")
    df = df[['Triage_Datetime']]


    print(df.head(5))

    df.to_excel('C:\\Users\\Hp\\OneDrive\\FYP\\ts_data.xlsx')