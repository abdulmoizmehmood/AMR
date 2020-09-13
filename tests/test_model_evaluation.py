import pytest
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from src.model_evaluation import evaluate_model

def test_evaluate_model():
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
    
    model = LogisticRegression()
    X = df.drop('sensitivity', axis=1)
    y = df['sensitivity']
    model.fit(X, y)
    
    joblib.dump(model, 'models/logistic_regression.joblib')
    
    evaluate_model('models/logistic_regression.joblib', df)
    
    y_pred_proba = model.predict_proba(X)[:, 1]
    auc = roc_auc_score(y, y_pred_proba)
    
    assert auc > 0.5, "AUC is less than 0.5, model evaluation failed"
