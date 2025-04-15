from fastapi import FastAPI
import joblib
import pandas as pd
import os
from schemas import PropertyData  # Import the schema from schemas.py

# Build the correct path to the model file
model_path = os.path.join(os.path.dirname(__file__), "model", "best_rent_model.pkl")

# Load the trained model using the correct path
model = joblib.load(model_path)

# Initialize the FastAPI app
app = FastAPI()

# Define the prediction endpoint
@app.post("/predict")
def predict_rent(data: PropertyData):
    # Convert the input data to a dictionary and then to a DataFrame
    input_data = data.dict()
    input_df = pd.DataFrame([input_data])

    # Predict rent
    predicted_rent = model.predict(input_df)

    # Return the prediction
    return {"predicted_rent": int(predicted_rent[0])}
