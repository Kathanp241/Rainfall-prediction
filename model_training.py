import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset
data = {
    "Temperature": [30, 28, 32, 25, 27, 33, 26, 29],
    "Humidity":    [85, 78, 90, 70, 65, 95, 60, 75],
    "WindSpeed":   [12, 10, 15, 8, 7, 18, 6, 9],
    "Rainfall":    [5.2, 3.1, 6.0, 2.0, 0.5, 7.5, 0.2, 3.5]
}

df = pd.DataFrame(data)

# Prepare data
X = df[['Temperature', 'Humidity', 'WindSpeed']]
y = df['Rainfall']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("models/weather_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
