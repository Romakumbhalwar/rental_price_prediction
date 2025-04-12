import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI
from app.schemas import RentalInput
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("app/model/best_linear_model.pkl")
encoders = joblib.load("app/model/encoders.pkl")
scaler = joblib.load("app/model/scaler.pkl")

@app.post("/predict")
def predict_price(data: RentalInput):
    input_dict = data.dict()

    for col in encoders:
        if col in input_dict:
            value = input_dict[col]
            if value in encoders[col].classes_:
                input_dict[col] = encoders[col].transform([value])[0]
            else:
                return {"error": f"Invalid value '{value}' for column '{col}'"}

    df = pd.DataFrame([input_dict])
    df_scaled = scaler.transform(df)

    prediction = model.predict(df_scaled)[0]
    return {"predicted_price": round(prediction, 2)}
