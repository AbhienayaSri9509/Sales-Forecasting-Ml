# 📊 Sales Forecasting App

This is a simple interactive web app built with **Streamlit** for uploading sales data and forecasting future sales using **Facebook Prophet**.

---

## 🚀 Features

- Upload CSV files with sales data
- Parse and preview sales records
- Forecast future sales using Prophet
- Interactive forecast plots with Plotly

---

## 🗂️ File Structure

sales_forecast_project/
│
├── app/                   # Streamlit app code
│   └── streamlit_app.py
│
├── data/                  # Input or example CSV files
│   └── sales_data.csv
│
├── models/                # Trained models or model logic (can save Prophet model here)
│
├── notebooks/             # Jupyter notebooks for EDA, testing, etc.
│   └── EDA.ipynb
│
├── src/                   # Source code (modular Python scripts)
│   ├── evaluate.py        # Evaluation logic (e.g., MAPE, RMSE)
│   ├── preprocessing.py   # Data cleaning and transformation
│   └── train.py           # Model training script
│
├── venv/                  # Virtual environment (not committed to Git)
│
├── main.py                # Entry point to launch the app
├── requirements.txt       # Python dependencies
└── README.md     

## ⚙️ Installation

1. **Clone the repo:**

git clone https://github.com/AbhienayaSri9509/Sales-Forecasting-Ml.git
cd sales-forecast_project

Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows

**Install dependencies:**

pip install -r requirements.txt

Run the app:

python main.py

**Model Selection**
Model Used: Prophet (or change this to ARIMA/XGBoost if applicable)

Why?

Handles seasonality and trend well

Easy to interpret and tune

Ideal for time-series forecasting with daily/weekly data

**Evaluation Metrics**
Metric	                       Value(example)
MAE (Mean Absolute Error)	    124.78
RMSE (Root Mean Square Error)	167.45
R² Score	                     0.84

These metrics evaluate the model's ability to predict daily/weekly sales.

**Dataset Information**
Source: Kaggle - Retail Sales Forecasting Dataset

License: Open use for educational/research

**Columns Used for Modeling**
ColumnName	           Description
date	              Date of the sale
product_id	          Unique product identifier
category	          Product category
units_sold	          Number of units sold on that date
price	              Price per unit

Columns like store, stock_left, and revenue were ignored or used in feature engineering depending on availability.

**Input CSV Format**
Ensure your CSV file contains:

A date column (e.g., Order Date)

A numeric sales column (e.g., Sales)

Example:

Order Date	Sales
2024-01-01	1250
2024-01-02	1400

**Transformations & Cleaning**
Handled missing dates via forward filling

Aggregated sales by product per day

Converted date to datetime format

Created features like:

Day of week

Month

Lag values (previous week's sales)

Normalized units_sold for model training

**📈 Forecasting Details**
Uses Facebook Prophet

Default forecast: 30 days into the future

Customizable aggregation and model options available in model/

**Why This Dataset?**
Contains realistic multi-product, multi-month sales

Supports time-based modeling

Helps simulate a real POS scenario for inventory optimization

**🧪 Development**
Exploratory notebooks in notebooks/

Modular model logic in model/

Extendable Streamlit interface in app/

**🧑‍💻 Author**
Abhienaya Sri

