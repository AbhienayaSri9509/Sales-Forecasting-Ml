import pandas as pd
from prophet import Prophet
import joblib
import os

def prepare_data(df, date_col='Order Date', sales_col='Sales'):
    """Prepare data for Prophet: select columns, rename, convert date."""
    df = df[[date_col, sales_col]].copy()
    df.columns = ['ds', 'y']
    df['ds'] = pd.to_datetime(df['ds'])
    return df

def train_and_save_model(csv_path, model_path='models/prophet_model.pkl'):
    """Train Prophet model from CSV and save it to disk."""
    # Load CSV
    df = pd.read_csv(csv_path, encoding='latin1')
    
    # Prepare data
    df_prepared = prepare_data(df)
    
    # Initialize and train model
    model = Prophet()
    model.fit(df_prepared)
    
    # Create models folder if doesn't exist
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    # Save model
    joblib.dump(model, model_path)
    print(f"Model trained and saved at {model_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Train Prophet model on sales data CSV.")
    parser.add_argument("--csv", type=str, required=True, help="Path to sales CSV file")
    parser.add_argument("--model-path", type=str, default="models/prophet_model.pkl", help="Path to save trained model")
    
    args = parser.parse_args()
    
    train_and_save_model(args.csv, args.model_path)
