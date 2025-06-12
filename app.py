import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(X_train)  # If you had real training data
scaled_input = scaler.transform(input_data)

# Dummy model with 5 input features (for demo only)
model = LinearRegression()
# Adjusted dummy model with balanced coefficients
model.coef_ = np.array([0.05, 0.1, 0.03, 0.005, 0.02])
model.intercept_ = 0.5


# App Title
st.title("🌧️ Rainfall Prediction")
st.markdown("Predict **rainfall (in mm)** using weather parameters powered by a basic ML model.")

# Input widgets
st.header("🌡️ Enter Weather Parameters")

col1, col2, col3 = st.columns(3)
with col1:
    temp = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
    wind_speed = st.number_input("Wind Speed (km/h)", 0.0, 100.0, 10.0)
with col2:
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 70.0)
    pressure = st.number_input("Pressure (hPa)", 900.0, 1100.0, 1013.0)
with col3:
    cloud_cover = st.number_input("Cloud Cover (%)", 0.0, 100.0, 50.0)

# Predict Button
if st.button("📊 Predict Rainfall"):
    input_data = np.array([[temp, humidity, wind_speed, pressure, cloud_cover]])
    prediction = model.predict(input_data)[0]

    # Interpretation
    if prediction < 1:
        rain_type = "☀️ No Rain"
        color = "green"
    elif prediction < 10:
        rain_type = "🌦️ Light Rain"
        color = "orange"
    else:
        rain_type = "🌧️ Heavy Rain"
        color = "red"

    # Output
    st.subheader("🔍 Prediction Result")
    st.markdown(f"### 🌧️ **Predicted Rainfall:** `{prediction:.2f} mm`")
    st.markdown(f"### 🌈 **Interpretation:** `{rain_type}`")
