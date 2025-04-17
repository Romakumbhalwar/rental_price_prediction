from fastapi import FastAPI
import joblib
import pandas as pd
import os
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Enable CORS (helpful when calling API from Streamlit or web frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Correct the path to the model file (it is located in the root directory)
model_path = os.path.join(os.path.dirname(__file__), "..", "best_rent_model.pkl")

# Load the trained model
try:
    model = joblib.load(model_path)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

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

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Rental Price Prediction API. Use /predict to get predictions."}

# Prediction endpoint in FastAPI
@app.post("/predict")
def predict_rent(data: PropertyData):
    if model is None:
        return {"error": "Model is not loaded properly"}

    # Convert input data to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Predict rent
    try:
        predicted_rent = model.predict(input_df)
        return {"predicted_rent": int(predicted_rent[0])}
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}
