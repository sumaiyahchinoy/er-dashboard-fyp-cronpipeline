
def medner(data):
    import pandas as pd
    from writeto_onedrive import write_to_onedrive    
    import en_ner_bc5cdr_md
    from append_data import append_new_data
    
    sci_nlp = en_ner_bc5cdr_md.load()

    #Components on NLP object (contains NER)
    sci_nlp.component_names

    # Explore entities (chemicals and diseases)
    sci_nlp.get_pipe('ner').labels

    new_df = data
    new_df['HOPI'] = new_df['HOPI'].str.lower()
    new_df["Diagnosis"] = ""
    # new_df.head()

    #create a null dataset
    df_null = new_df[new_df['HOPI'].isna()]
    # df_null.head()
    len(df_null)

    #create a non null dataset
    df_diagnosis = new_df.dropna(axis=0, subset=['HOPI'])
    len(df_diagnosis)

    for index, row in df_diagnosis.iterrows():
        print(index)
        print(row['HOPI'])
        text = row['HOPI']
        docx = sci_nlp(text)
        for ent in docx.ents:
            print(ent.text, ent.label_)
            if (ent.label_ == 'DISEASE'):
                df_diagnosis.at[index, "Diagnosis"] =  row["Diagnosis"] + ent.text + ','
        print("Diagnosis: ")
        print(row["Diagnosis"])
        # row["Diagnosis"] = doc.ents

    df = df_diagnosis.append(df_null)
    df = df.sort_index()
    df = df['Diagnosis'].map(lambda x: str(x)[:-2])
    # len(df)
    
    # write_to_onedrive(df, 'cleaned_dataset.xlsx')
    append_new_data(df)