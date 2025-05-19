import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# === Load Model and Scaler ===
@st.cache_resource
def load_model():
    model = joblib.load('aqi_city_rf_model1.pkl')
    scaler = joblib.load('scaler_city1.pkl')
    return model, scaler

rf_model_city, scaler_city = load_model()

# === Title and Description ===
st.title("Air Quality Index (AQI) Prediction")
st.write("Predict AQI based on pollutant data using a Random Forest model.")

# === Input Fields ===
st.sidebar.header("Enter Pollutant Data:")

pm25 = st.sidebar.number_input("PM2.5 (μg/m³):", min_value=0.0, value=10.0)
pm10 = st.sidebar.number_input("PM10 (μg/m³):", min_value=0.0, value=20.0)
no2 = st.sidebar.number_input("NO2 (μg/m³):", min_value=0.0, value=15.0)
co = st.sidebar.number_input("CO (mg/m³):", min_value=0.0, value=0.5)
so2 = st.sidebar.number_input("SO2 (μg/m³):", min_value=0.0, value=5.0)
o3 = st.sidebar.number_input("O3 (μg/m³):", min_value=0.0, value=30.0)
year = st.sidebar.number_input("Year:", min_value=2020, max_value=2030, value=2025)
month = st.sidebar.number_input("Month:", min_value=1, max_value=12, value=5)
day = st.sidebar.number_input("Day:", min_value=1, max_value=31, value=10)

# === Prediction Button ===
if st.button("Predict AQI"):
    # Collect input data
    input_data = np.array([[pm25, pm10, no2, co, so2, o3, year, month, day]])
    
    # Scale the input data
    input_scaled = scaler_city.transform(input_data)
    
    # Predict
    prediction = rf_model_city.predict(input_scaled)
    predicted_aqi = prediction[0]
    
    # Display Prediction
    st.subheader(f"Predicted AQI: {predicted_aqi:.2f}")

    # Interpretation of AQI
    if predicted_aqi <= 50:
        st.success("Good - Air quality is considered satisfactory, and air pollution poses little or no risk.")
    elif 51 <= predicted_aqi <= 100:
        st.info("Moderate - Air quality is acceptable; however, some pollutants may be a concern for a small number of people.")
    elif 101 <= predicted_aqi <= 150:
        st.warning("Unhealthy for Sensitive Groups - Members of sensitive groups may experience health effects.")
    elif 151 <= predicted_aqi <= 200:
        st.warning("Unhealthy - Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.")
    elif 201 <= predicted_aqi <= 300:
        st.error("Very Unhealthy - Health alert: everyone may experience more serious health effects.")
    else:
        st.error("Hazardous - Health warning of emergency conditions.")
