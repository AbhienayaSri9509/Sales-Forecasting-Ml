import streamlit as st
import pandas as pd
from models.train import train_model
from models.preprocessing import prepare_data
from prophet.plot import plot_plotly, plot_components_plotly

st.set_page_config(page_title="Sales Forecasting App")

st.title("📊 Sales Forecasting App")
st.write("Upload a CSV file for prediction")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, encoding='latin1')
        st.success("✅ File uploaded and read successfully!")
        st.subheader("Preview of your data:")
        st.dataframe(df.head())

        # Prepare data
        df_prepared = prepare_data(df)

        # Train model
        model = train_model(df_prepared)

        # Forecast horizon input
        periods_input = st.number_input(
            "Enter forecast horizon (days)", min_value=1, max_value=365, value=30)

        # Make forecast
        forecast = model.predict(model.make_future_dataframe(periods=periods_input))

        # Display forecast
        st.subheader(f"Forecast for next {periods_input} days")
        fig1 = plot_plotly(model, forecast)
        st.plotly_chart(fig1)

        # Display components
        st.subheader("Forecast Components")
        fig2 = plot_components_plotly(model, forecast)
        st.plotly_chart(fig2)

    except Exception as e:
        st.error(f"Error processing the file: {e}")

else:
    st.info("Please upload a CSV file to get started.")
