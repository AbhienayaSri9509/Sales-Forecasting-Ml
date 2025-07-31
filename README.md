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

git clone https://github.com/your-username/sales-forecasting-app.git
cd sales-forecast_project

Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows

**Install dependencies:**

pip install -r requirements.txt

Run the app:

python main.py


**Input CSV Format**
Ensure your CSV file contains:

A date column (e.g., Order Date)

A numeric sales column (e.g., Sales)

Example:

Order Date	Sales
2024-01-01	1250
2024-01-02	1400

**📈 Forecasting Details**
Uses Facebook Prophet

Default forecast: 30 days into the future

Customizable aggregation and model options available in model/

**🧪 Development**
Exploratory notebooks in notebooks/

Modular model logic in model/

Extendable Streamlit interface in app/

**🧑‍💻 Author**
Abhienaya Sri

