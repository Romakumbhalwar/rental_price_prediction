from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

# Load the pre-trained model
loaded_model = joblib.load('app/model/best_rent_model.pkl')

app = FastAPI()

# Schema for the input data
class RentPredictionRequest(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    property_type: str
    size_in_sqft: float
    bedrooms: int
    bathrooms: int
    balcony: int
    furnishing_status: str
    number_of_amenities: int

# Prediction endpoint
@app.post("/predict/")
def predict(request: RentPredictionRequest):
    # Prepare the input data
    new_data = pd.DataFrame([{
        'city': request.city,
        'area': request.area,
        'location': request.location,
        'zone': request.zone,
        'property_type': request.property_type,
        'size_in_sqft': request.size_in_sqft,
        'bedrooms': request.bedrooms,
        'bathrooms': request.bathrooms,
        'balcony': request.balcony,
        'furnishing_status': request.furnishing_status,
        'number_of_amenities': request.number_of_amenities
    }])

    # Predict using the trained model
    predicted_rent = loaded_model.predict(new_data)
    return {"predicted_rent": round(predicted_rent[0], 2)}

