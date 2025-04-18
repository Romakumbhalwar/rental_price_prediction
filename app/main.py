from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()

# Define the path to the model
model_path = "app/model/best_rent_model.pkl"  # Updated model path

# Load the model
try:
    # Check if model file exists
    if os.path.exists(model_path):
        model_dict = joblib.load(model_path)
        model = model_dict["model"]
        features = model_dict["features"]
        print(f"✅ Model loaded successfully: {type(model)}")
    else:
        raise FileNotFoundError(f"Model file {model_path} not found.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None
    features = None

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

# POST route only
@app.post("/predict")
def predict_rent(data: PropertyData):
    if model is None:
        return {"error": "Model not loaded."}
    
    input_df = pd.DataFrame([data.dict()])

    try:
        # Make prediction using the loaded model
        prediction = model.predict(input_df)
        return {"predicted_rent": int(prediction[0])}
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}
