import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Forecasting App", layout="centered")

st.title("📊 Sales Forecasting App")
st.write("Upload a CSV file for prediction")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Read and display CSV content
if uploaded_file is not None:
    try:
        # Read CSV using a more forgiving encoding
        df = pd.read_csv(uploaded_file, encoding='latin1')

        st.success("✅ File uploaded and read successfully!")
        st.subheader("Preview of your data:")
        st.dataframe(df.head())

        # You can add forecasting code here

    except Exception as e:
        st.error(f"❌ An error occurred while reading the file:\n\n{e}")
