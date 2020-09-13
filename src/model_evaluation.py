import pandas as pd
from sklearn.metrics import roc_auc_score, classification_report
import joblib

def load_data(file_path):
    return pd.read_csv(file_path)

def evaluate_model(model_path, df):
    model = joblib.load(model_path)
    X = df.drop('sensitivity', axis=1)
    y = df['sensitivity']
    
    y_pred = model.predict(X)
    y_pred_proba = model.predict_proba(X)[:, 1]
    
    auc = roc_auc_score(y, y_pred_proba)
    report = classification_report(y, y_pred)
    
    print(f'Model: {model_path}')
    print(f'AUC: {auc:.4f}')
    print('Classification Report:')
    print(report)

if __name__ == "__main__":
    data_path = 'data/processed_data.csv'
    df = load_data(data_path)
    
    model_paths = ['models/logistic_regression.joblib', 'models/random_forest.joblib', 'models/gradient_boosting.joblib', 'models/neural_network.joblib']
    for model_path in model_paths:
        evaluate_model(model_path, df)
