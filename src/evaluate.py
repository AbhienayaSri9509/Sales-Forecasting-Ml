from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def evaluate_model(y_test, y_pred):
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("\nModel Evaluation Metrics:")
    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R² Score: {r2:.2f}")

# Optional: If you want to run this standalone
if __name__ == "__main__":
    import joblib
    import pandas as pd

    # Load test data and model
    model = joblib.load("../models/model.pkl")
    test_df = pd.read_csv("../data/test.csv")
    
    X_test = test_df.drop("sales", axis=1)
    y_test = test_df["sales"]
    
    y_pred = model.predict(X_test)

    evaluate_model(y_test, y_pred)
