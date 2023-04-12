import sys
import pandas as pd

sys.path.insert(0, "..")

import spacy
from spacy.tokens import Span

import medspacy
from medspacy.preprocess import PreprocessingRule, Preprocessor
from medspacy.ner import TargetRule
from medspacy.context import ConTextRule
from medspacy.section_detection import Sectionizer
from medspacy.postprocess import PostprocessingRule, PostprocessingPattern, Postprocessor
from medspacy.postprocess import postprocessing_functions
from medspacy.visualization import visualize_ent, visualize_dep

import re

df = pd.read_excel('C:/Users/lenovo/Downloads/Adult 2021 Anonymized.xlsx')
df = df[['ED_DX']]
df = df.dropna()
df["Diagnosis"] = ''

nlp = medspacy.load("en_core_med7_trf")


nlp.pipe_names
ner = nlp.get_pipe("ner")
ner.labels

preprocessor = Preprocessor(nlp.tokenizer)
nlp.tokenizer = preprocessor

preprocess_rules = [
    
    PreprocessingRule(
        r"\[\*\*[\d]{1,4}-[\d]{1,2}(-[\d]{1,2})?\*\*\]",
        repl="01-01-2010",
        desc="Replace MIMIC date brackets with a generic date."
    ),
    
    PreprocessingRule(
        r"\[\*\*[\d]{4}\*\*\]",
        repl="2010",
        desc="Replace MIMIC year brackets with a generic year."
    ),
    
    PreprocessingRule(
        r"dx'd", 
        repl="Diagnosed", 
        desc="Replace abbreviation"
    ),
    
    PreprocessingRule(
        r"tx'd", 
        repl="Treated", 
        desc="Replace abbreviation"
    ),
    
    PreprocessingRule(
        r"\[\*\*[^\]]+\]", 
        desc="Remove all other bracketed placeholder text from MIMIC"
    )
]

preprocessor.add(preprocess_rules)

target_rules = [
    TargetRule(literal="abdominal pain", category="PROBLEM"),
    TargetRule("stroke", "PROBLEM"),
    TargetRule("hemicolectomy", "TREATMENT"),
    TargetRule("colon cancer", "PROBLEM"),
    TargetRule("radiotherapy", "PROBLEM",
            pattern=[{"LOWER": "xrt"}]),
    TargetRule("metastasis", "PROBLEM"),
    TargetRule("cough", "PROBLEM"),
    TargetRule("Type II Diabetes Mellitus", "PROBLEM", 
            pattern=[
                {"LOWER": "type"},
                {"LOWER": {"IN": ["2", "ii", "two"]}},
                {"LOWER": {"IN": ["dm", "diabetes"]}},
                {"LOWER": "mellitus", "OP": "?"}
            ],),
    TargetRule("Hypertension", "PROBLEM",
            pattern=[{"LOWER": {"IN": ["htn", "hypertension"]}}],),
]

target_matcher = nlp.get_pipe("medspacy_target_matcher")
target_matcher.add(target_rules)

context = nlp.get_pipe("medspacy_context")
context_rules = [
ConTextRule("diagnosed in <YEAR>", "HISTORICAL", 
            pattern=[
                {"LOWER": "diagnosed"},
                {"LOWER": "in"},
                {"LOWER": {"REGEX": "^[\d]{4}$"}}
            ])
]

nlp.pipe_names

for index, row in df.iterrows():
    print(index)
    print(row['ED_DX'])
    text = row['ED_DX']
    doc = nlp(text)
    print("Entities After Text Processing")
    print(doc.ents)
    row["Diagnosis"] = doc.ents
    print("Diagnosis: ")
    print(row["Diagnosis"])
