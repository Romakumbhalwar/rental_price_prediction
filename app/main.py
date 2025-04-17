from fastapi import FastAPI
import joblib
import pandas as pd
import os
from app.schemas import PropertyData  # Import the schema from schemas.py
from fastapi.middleware.cors import CORSMiddleware

# Correct the path to the model file (it is located in the root directory)
model_path = os.path.join(os.path.dirname(__file__), "..", "best_rent_model.pkl")

# Load the trained model
try:
    model = joblib.load(model_path)
    print(f"✅ Model loaded successfully: {type(model)}")  # Debugging print: Check the model type
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# Initialize the FastAPI app
app = FastAPI()

# Enable CORS (helpful when calling API from Streamlit or web frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Rental Price Prediction API. Use /predict to get predictions."}

# Define the prediction endpoint
@app.post("/predict")
def predict_rent(data: PropertyData):
    if model is None:
        return {"error": "Model is not loaded properly"}

    # Convert input data to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Predict rent
    try:
        # Debugging print: Check the type of the model and input
        print(f"Model type: {type(model)}")
        print(f"Input data: {input_df.head()}")
        
        # Ensure model.predict() is called on the correct model
        predicted_rent = model.predict(input_df)
        print(f"Predicted rent: {predicted_rent}")  # Debugging print
        
        return {"predicted_rent": int(predicted_rent[0])}
    except Exception as e:
        print(f"Error during prediction: {e}")  # Add debugging print statement
        return {"error": f"Prediction failed: {e}"}
