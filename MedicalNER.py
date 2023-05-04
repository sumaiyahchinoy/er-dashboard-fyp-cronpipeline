# %%
# Load Packages
import pandas as pd
# import sys
# import spacy
import en_ner_bc5cdr_md
sci_nlp = en_ner_bc5cdr_md.load()
import re

# %%
#Components on NLP object (contains NER)
sci_nlp.component_names

# %%
# Explore entities (chemicals and diseases)
sci_nlp.get_pipe('ner').labels

# %%
# df = pd.read_excel('https://1drv.ms/x/s!AsCp_kE1E5Md6UkKXCAorwdeI3bi?e=SGPCLs')
from access_onedrive import create_onedrive_directdownload

onedrive_link = 'https://1drv.ms/x/s!AsCp_kE1E5Md6UkKXCAorwdeI3bi?e=SGPCLs'
link = create_onedrive_directdownload(onedrive_link)
new_df = pd.read_excel(link)



# %%
new_df['HOPI'] = new_df['HOPI'].str.lower()
new_df["Diagnosis"] = ""
# new_df.head()

# %%
#create a null dataset
df_null = new_df[new_df['HOPI'].isna()]
# df_null.head()
len(df_null)

# %%
#create a non null dataset
df_diagnosis = new_df.dropna(axis=0, subset=['HOPI'])
len(df_diagnosis)

# %%
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
    
# df.iloc[1:20000].to_excel('diagnosis_1.xlsx')
# df.iloc[20001:40000].to_excel('diagnosis_2.xlsx')

# %%
# df = pd.concat(df_diagnosis, df_null, join="outer")
df = df_diagnosis.append(df_null)
df = df.sort_index()
df = df['Diagnosis'].map(lambda x: str(x)[:-2])
# len(df)