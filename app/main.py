from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()

# Define the input data schema
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

# Load the trained model
model_path = os.path.join("app", "model", "best_rent_model.pkl")

try:
    model = joblib.load(model_path)  # ✅ Load model directly
    print(f"✅ Model loaded successfully: {type(model)}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# Prediction endpoint
@app.post("/predict")
def predict_rent(data: PropertyData):
    if model is None:
        return {"error": "Model is not loaded properly"}

    # Convert input data to DataFrame
    input_df = pd.DataFrame([data.dict()])

    try:
        # Predict rent
        predicted_rent = model.predict(input_df)
        return {"predicted_rent": int(predicted_rent[0])}
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}
