import pandas as pd

def prepare_data(df, date_col='Order Date', sales_col='Sales'):
    """
    Prepare raw sales DataFrame for Prophet.
    
    Parameters:
    - df: pandas DataFrame with raw sales data
    - date_col: name of the date column (default 'Order Date')
    - sales_col: name of the sales column (default 'Sales')
    
    Returns:
    - cleaned pandas DataFrame with columns ['ds', 'y'] suitable for Prophet
    """
    # Check required columns exist
    if date_col not in df.columns or sales_col not in df.columns:
        raise ValueError(f"Input DataFrame must contain '{date_col}' and '{sales_col}' columns")

    # Drop rows where date or sales is missing
    df_clean = df[[date_col, sales_col]].dropna()

    # Convert date column to datetime
    df_clean[date_col] = pd.to_datetime(df_clean[date_col], errors='coerce')

    # Drop rows where date conversion failed
    df_clean = df_clean.dropna(subset=[date_col])

    # Aggregate sales by date (in case of duplicates)
    df_agg = df_clean.groupby(date_col)[sales_col].sum().reset_index()

    # Rename columns for Prophet
    df_agg = df_agg.rename(columns={date_col: 'ds', sales_col: 'y'})

    # Sort by date
    df_agg = df_agg.sort_values(by='ds').reset_index(drop=True)

    return df_agg
