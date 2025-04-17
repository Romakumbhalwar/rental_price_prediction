from fastapi import FastAPI
import joblib
import pandas as pd
import os
from schemas import PropertyData  # Import the schema from schemas.py
from fastapi.middleware.cors import CORSMiddleware

# Build the correct path to the model file
model_path = os.path.join(os.path.dirname(__file__), "model", "best_rent_model.pkl")

# Load the trained model
try:
    model = joblib.load(model_path)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Initialize the FastAPI app
app = FastAPI()

# Enable CORS if you are testing from a different origin (e.g., Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Define the prediction endpoint
@app.post("/predict")
def predict_rent(data: PropertyData):
    if model is None:
        return {"error": "Model is not loaded properly"}

    # Convert the input data to a dictionary and then to a DataFrame
    input_data = data.dict()
    input_df = pd.DataFrame([input_data])

    # Predict rent
    try:
        predicted_rent = model.predict(input_df)
        return {"predicted_rent": int(predicted_rent[0])}
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}
