# models/prophet_model.py

from prophet import Prophet
import pandas as pd

def prepare_data(df, date_col='Order Date', sales_col='Sales'):
    """Clean and prepare the DataFrame for Prophet."""
    df[date_col] = pd.to_datetime(df[date_col])
    daily_sales = df.groupby(date_col)[sales_col].sum().reset_index()
    daily_sales.columns = ['ds', 'y']  # Prophet expects these column names
    return daily_sales

def train_model(df):
    """Train a Prophet model and return forecast."""
    model = Prophet()
    model.fit(df)
    return model

def make_forecast(model, periods=30):
    """Generate a future forecast."""
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast
