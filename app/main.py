from fastapi import FastAPI
from app.schemas import RentInput
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("app/best_rent_model.pkl")

@app.get("/")
def read_root():
    return {"message": "Rental Price Prediction API is live!"}

@app.post("/predict")
def predict_rent(data: RentInput):
    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data)
    return {"predicted_rent": prediction[0]}
