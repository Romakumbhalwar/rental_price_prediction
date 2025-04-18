from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load the model
try:
    model_dict = joblib.load("best_rent_model.pkl")
    model = model_dict["model"]
    features = model_dict["features"]
    print(f"✅ Model loaded successfully: {type(model)}")
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
        prediction = model.predict(input_df)
        return {"predicted_rent": int(prediction[0])}
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}
