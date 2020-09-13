import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import roc_auc_score
import joblib

def load_data(file_path):
    return pd.read_csv(file_path)

def train_models(df):
    X = df.drop('sensitivity', axis=1)
    y = df['sensitivity']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    models = {
        'logistic_regression': LogisticRegression(),
        'random_forest': RandomForestClassifier(),
        'gradient_boosting': GradientBoostingClassifier(),
        'neural_network': MLPClassifier()
    }
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, y_pred)
        print(f'{name} AUC: {auc:.4f}')
        joblib.dump(model, f'models/{name}.joblib')
        
    return models

if __name__ == "__main__":
    data_path = 'data/processed_data.csv'
    df = load_data(data_path)
    train_models(df)
