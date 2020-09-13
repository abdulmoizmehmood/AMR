import pytest
import pandas as pd
from src.model_training import train_models

def test_train_models():
    data = {
        'age': [25, 35],
        'height': [175, 160],
        'weight': [70, 60],
        'admission_time': [1000, 2000],
        'culture_time': [1500, 2500],
        'gender_Female': [0, 1],
        'gender_Male': [1, 0],
        # Add other encoded categorical columns...
        'sensitivity': [0, 1]
    }
    
    df = pd.DataFrame(data)
    models = train_models(df)
    
    assert 'logistic_regression' in models, "Logistic Regression model not trained"
    assert 'random_forest' in models, "Random Forest model not trained"
    assert 'gradient_boosting' in models, "Gradient Boosting model not trained"
    assert 'neural_network' in models, "Neural Network model not trained"
