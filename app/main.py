from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()

# Load model
model = None
try:
    model_data = joblib.load("app/model/best_rent_model.pkl")  # adjust if path is different
    model = model_data["model"]  # ✅ extract the model from dict
    print("✅ Model loaded successfully:", type(model))
except Exception as e:
    print("❌ Error loading model:", e)

# Input schema
class PropertyData(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    property_type: str
    size_in_sqft: int
    bedrooms: int
    bathrooms: int
    balcony: int
    furnishing_status: str
    number_of_amenities: int

@app.post("/predict")
def predict_rent(data: PropertyData):
    if model is None:
        return {"error": "Model is not loaded properly"}

    input_df = pd.DataFrame([data.dict()])
    
    try:
        predicted_rent = model.predict(input_df)
        return {"predicted_rent": int(predicted_rent[0])}
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}
