import pytest
import pandas as pd
from src.data_preprocessing import preprocess_data

def test_preprocess_data():
    data = {
        'age': [25, 35],
        'gender': ['Male', 'Female'],
        'ethnicity': ['Ethnicity1', 'Ethnicity2'],
        'height': [175, 160],
        'weight': [70, 60],
        'unit_location': ['Location1', 'Location2'],
        'unit_type': ['Type1', 'Type2'],
        'admission_source': ['Source1', 'Source2'],
        'admission_time': [1000, 2000],
        'diagnosis': ['Diagnosis1', 'Diagnosis2'],
        'culture_time': [1500, 2500],
        'culture_site': ['Site1', 'Site2'],
        'organism': ['Organism1', 'Organism2'],
        'antibiotic': ['Antibiotic1', 'Antibiotic2'],
        'sensitivity': ['Sensitive', 'Resistant']
    }
    
    df = pd.DataFrame(data)
    processed_df = preprocess_data(df)
    
    assert not processed_df.isnull().values.any(), "Preprocessed data contains null values"
    assert 'sensitivity' in processed_df.columns, "Target variable 'sensitivity' not in processed data"
