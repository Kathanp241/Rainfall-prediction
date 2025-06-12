import streamlit as st
import pickle
import numpy as np
import os
import datetime

@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'models/weather_model.pkl')
    with open(model_path, 'rb') as f:
        return pickle.load(f)

model_data = load_model()
model = model_data['model']
scaler = model_data['scaler']

# App Title and Description
st.title('🌦️ Rainfall Prediction App')
st.markdown("Enter the weather parameters below to estimate the **rainfall amount (in mm)**.")

# Input Section
st.sidebar.header("🌡️ Weather Input Parameters")
temp = st.sidebar.slider('Temperature (°C)', -10.0, 50.0, 25.0)
humidity = st.sidebar.slider('Humidity (%)', 0.0, 100.0, 60.0)
wind_speed = st.sidebar.slider('Wind Speed (km/h)', 0.0, 100.0, 10.0)
pressure = st.sidebar.slider('Pressure (hPa)', 900.0, 1100.0, 1013.0)
cloud_cover = st.sidebar.slider('Cloud Cover (%)', 0.0, 100.0, 50.0)

# Main Content Section
if st.button('🔍 Predict Rainfall'):
    input_features = np.array([[temp, humidity, wind_speed, pressure, cloud_cover]])
    scaled_input = scaler.transform(input_features)
    prediction = model.predict(scaled_input)[0]

    # Interpretation
    if prediction < 1:
        rain_type = "☀️ No Rain"
        color = "green"
    elif prediction < 10:
        rain_type = "🌦️ Light Rain"
        color = "yellow"
    else:
        rain_type = "🌧️ Heavy Rain"
        color = "red"

    # Result Display
    st.subheader("📊 Prediction Result")
    st.metric(label="Predicted Rainfall (mm)", value=f"{prediction:.2f}", delta=rain_type)

    st.progress(min(1.0, prediction / 50.0))  # Max rainfall assumed ~50 mm

    # Downloadable Report
    report = (
        f"Rainfall Prediction Report\n"
        f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        f"Inputs:\n"
        f"Temperature: {temp} °C\n"
        f"Humidity: {humidity} %\n"
        f"Wind Speed: {wind_speed} km/h\n"
        f"Pressure: {pressure} hPa\n"
        f"Cloud Cover: {cloud_cover} %\n\n"
        f"Predicted Rainfall: {prediction:.2f} mm\n"
        f"Interpretation: {rain_type}\n"
    )
    st.download_button("📄 Download Prediction Report", report, file_name="rainfall_report.txt")
