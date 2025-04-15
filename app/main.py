from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from schemas import PropertyData  # Import the schema from schemas.py

# Load the trained model (make sure the model file is in the correct location)
model = joblib.load('best_rent_model.pkl')  # Replace with the actual path to your saved model

app = FastAPI()

# Define the prediction endpoint
@app.post("/predict")
def predict_rent(data: PropertyData):
    # Convert the input data to a DataFrame
    input_data = data.dict()  # Convert Pydantic model to a dictionary
    input_df = pd.DataFrame([input_data])

    # Perform the prediction using the loaded model
    predicted_rent = model.predict(input_df)

    # Return the prediction as a response
    return {"predicted_rent": int(predicted_rent[0])}
