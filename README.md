🌧️ AI-Powered Rainfall Prediction

This project is a simple machine learning-based application that predicts **rainfall in millimeters** based on key weather parameters such as temperature, humidity, wind speed, pressure, and cloud cover. It is developed using Python and deployed as an interactive web app using **Streamlit**.


🚀 Project Overview

Rainfall forecasting is crucial in agriculture, disaster management, and public planning. This project demonstrates a basic regression model for rainfall prediction using synthetic or real weather data. The model takes live user input and provides rainfall estimates along with an interpretation (e.g., No Rain, Light Rain, or Heavy Rain).


🧠 Technologies & Tools Used

- **Python**
- **Streamlit** – for the web app UI
- **NumPy** – for numerical operations
- **Scikit-learn** – for Linear Regression
- **Matplotlib / Seaborn** (optional for visualization)


📥 Input Parameters

The user enters the following weather parameters:
- 🌡️ Temperature (°C)
- 💧 Humidity (%)
- 🌬️ Wind Speed (km/h)
- 🌪️ Pressure (hPa)
- ☁️ Cloud Cover (%)


🔍 How It Works

1. **Model**: A basic `LinearRegression` model from scikit-learn is used (you can replace it with any trained model).
2. **Feature Input**: User inputs real-time data using Streamlit sliders.
3. **Prediction**: Model predicts rainfall in mm.
4. **Output**: Result is displayed with interpretation and can be downloaded.


💻 Live Demo (Optional)
👉 Hosted on: https://rainfall-prediction-paxbfjxnuugaryq4z8dp43.streamlit.app/


🛠️ How to Run Locally

🔧 Prerequisites:
- Python 3.8+
- pip

📦 Install dependencies:
```bash
pip install streamlit scikit-learn numpy keras tensorflow
