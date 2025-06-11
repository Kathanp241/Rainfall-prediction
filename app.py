import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("models/weather_model.pkl", "rb"))

# App title
st.title("🌧️ Rainfall Prediction App")
st.markdown("Enter the weather conditions below to predict rainfall in millimeters (mm).")

# User Inputs
temp = st.number_input("🌡️ Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0, step=0.1)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.1)
wind_speed = st.number_input("🌬️ Wind Speed (km/h)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)

# Predict Button
if st.button("📊 Predict Rainfall"):
    input_data = np.array([[temp, humidity, wind_speed]])
    prediction = model.predict(input_data)
    st.success(f"🌦️ Predicted Rainfall: **{prediction[0]:.2f} mm**")
