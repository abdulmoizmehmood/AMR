
# Dummy Data Generation Due to public nature of this repo.

# Let's assume the data is stored in a CSV file with the following columns: `patient_id`, `age`, `gender`, `ethnicity`, `height`, `weight`, `unit_location`, `unit_type`, `admission_source`, `admission_time`, `diagnosis`, `culture_time`, `culture_site`, `organism`, `antibiotic`, `sensitivity`.


import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Handle missing values
    imputer = SimpleImputer(strategy='median')
    df[['height', 'weight']] = imputer.fit_transform(df[['height', 'weight']])
    
    # One-hot encode categorical variables
    categorical_features = ['gender', 'ethnicity', 'unit_location', 'unit_type', 'admission_source', 'diagnosis', 'culture_site', 'organism', 'antibiotic']
    encoder = OneHotEncoder(sparse=False)
    encoded_features = encoder.fit_transform(df[categorical_features])
    encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_features))
    
    # Scale numerical features
    numerical_features = ['age', 'height', 'weight', 'admission_time', 'culture_time']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[numerical_features])
    scaled_df = pd.DataFrame(scaled_features, columns=numerical_features)
    
    # Combine processed features
    processed_df = pd.concat([scaled_df, encoded_df], axis=1)
    
    # Add the target variable
    processed_df['sensitivity'] = df['sensitivity'].apply(lambda x: 1 if x == 'Resistant' else 0)
    
    return processed_df

if __name__ == "__main__":
    raw_data_path = 'data/raw_data.csv'
    processed_data_path = 'data/processed_data.csv'
    
    raw_df = load_data(raw_data_path)
    processed_df = preprocess_data(raw_df)
    processed_df.to_csv(processed_data_path, index=False)
