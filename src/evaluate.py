import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_forecast(y_true, y_pred):
    """
    Compute evaluation metrics for regression forecasts.
    
    Args:
        y_true (array-like): Actual values
        y_pred (array-like): Predicted values
        
    Returns:
        dict: MAE, RMSE, and R² scores
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    
    return {
        "MAE": round(mae, 2),
        "RMSE": round(rmse, 2),
        "R2 Score": round(r2, 2)
    }

def evaluate_on_dataframe(df, actual_col='y', predicted_col='yhat'):
    """
    Evaluate a forecast using a DataFrame with actual and predicted columns.

    Args:
        df (pd.DataFrame): DataFrame containing actual and predicted columns
        actual_col (str): Name of the column with actual values
        predicted_col (str): Name of the column with predicted values

    Returns:
        dict: Evaluation metrics
    """
    y_true = df[actual_col].values
    y_pred = df[predicted_col].values
    return evaluate_forecast(y_true, y_pred)

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv("data/test_predictions.csv")  # Ensure this has 'y' and 'yhat'
    results = evaluate_on_dataframe(df)
    print("Evaluation Results:")
    for k, v in results.items():
        print(f"{k}: {v}")
