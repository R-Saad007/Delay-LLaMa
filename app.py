from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import google.generativeai as genai

# ------------------------
# Load your ML model
# ------------------------
model = joblib.load("delay_model.pkl")

# ------------------------
# Configure Gemini
# ------------------------
genai.configure(api_key="AIzaSyB1pAobfiBIucyUfRS1wvfRQTNoxIgvVgE")
gemini = genai.GenerativeModel("gemini-2.0-flash")

# ------------------------
# Setup FastAPI
# ------------------------
app = FastAPI()

# ------------------------
# Input schema for POST requests
# ------------------------
class FlightInput(BaseModel):
    temp: float
    wind_speed: float
    visibility: float

# ------------------------
# Prediction + GenAI endpoint
# ------------------------
@app.post("/predict")
def predict_delay(data: FlightInput):
    # 1) Predict delay using ML
    prediction = model.predict([[data.temp, data.wind_speed, data.visibility]])[0]

    # 2) Generate natural language summary using Gemini
    prompt = f"""
    Given the weather conditions:
    - Temperature: {data.temp}°C
    - Wind Speed: {data.wind_speed} knots
    - Visibility: {data.visibility} km

    And a predicted flight delay of approximately {prediction:.1f} minutes,
    write a short friendly passenger advisory,
    plus a brief note for pilots on operational considerations.
    """

    response = gemini.generate_content(prompt)
    advisory = response.text

    # 3) Return as JSON
    return {
        "predicted_delay_min": round(prediction, 1),
        "advisory": advisory
    }
