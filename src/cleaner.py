import pandas as pd
import json
import os

RAW_PATH = os.path.join('data', 'raw_patients.csv')
CLEANED_PATH = os.path.join('data', 'cleaned_patients.csv')
ONTOLOGY_PATH = os.path.join('src', 'ontology_map.json')


raw_df = pd.read_csv(RAW_PATH)


if 'age' in raw_df.columns:
    raw_df['age'] = raw_df['age'].fillna(raw_df['age'].median())


if 'gender' in raw_df.columns:
    raw_df['gender'] = raw_df['gender'].fillna('Other')


if 'condition' in raw_df.columns:
    raw_df['condition'] = raw_df['condition'].fillna('Missing')


with open(ONTOLOGY_PATH, 'r') as f:
    ontology = json.load(f)

condition_map = {}
for std, synonyms in ontology.items():
    for s in synonyms:
        condition_map[s.strip().lower()] = std
    condition_map[std.strip().lower()] = std  

def standardize_condition(cond):
    if pd.isna(cond) or cond == 'Missing':
        return 'Missing'
    key = str(cond).strip().lower()
    return condition_map.get(key, cond)

raw_df['condition'] = raw_df['condition'].apply(standardize_condition)


raw_df.to_csv(CLEANED_PATH, index=False)

print(f"Cleaned data written to {CLEANED_PATH}")

