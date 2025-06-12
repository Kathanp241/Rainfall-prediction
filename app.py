import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Dummy model (for testing only)
model = LinearRegression()
model.coef_ = np.array([0.1, 0.05, 0.2])
model.intercept_ = 1.0

st.title("🌧️ Rainfall Prediction")
st.write('AI-Powered Model Predict rainfall based on weather parameters')

# Input widgets
col1, col2, col3 = st.columns(3)
with col1:
    temp = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
with col2:
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 70.0)
with col3:
    wind = st.number_input("Wind Speed (km/h)", 0.0, 50.0, 10.0)

# Predict Button
if st.button("📊 Predict Rainfall"):
    input_data = np.array([[temp, humidity, wind_speed]])
    prediction = model.predict(input_data)
    st.success(f"🌦️ Predicted Rainfall: **{prediction[0]:.2f} mm**")
