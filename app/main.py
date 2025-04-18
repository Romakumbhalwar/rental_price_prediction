from fastapi import FastAPI
from app.schemas import RentInput
import pandas as pd
import joblib

app = FastAPI()

# Load model and features
try:
    model_bundle = joblib.load("app/model/best_rent_model.pkl")
    model = model_bundle["model"]
    model_features = model_bundle["features"]
    print("✅ Model loaded successfully:", type(model))
except Exception as e:
    print("❌ Error loading model:", e)
    model = None
    model_features = []

@app.get("/")
def home():
    return {"message": "Rental Price Prediction API"}

@app.post("/predict")
def predict_rent(data: RentInput):
    try:
        # Convert request data to DataFrame
        input_df = pd.DataFrame([data.dict()])

        # Ensure feature order matches training
        input_df = input_df[model_features]

        # Ensure that all necessary columns are present
        missing_features = [col for col in model_features if col not in input_df.columns]
        if missing_features:
            return {"error": f"Missing features: {', '.join(missing_features)}"}

        # Make the prediction using the trained model
        prediction = model.predict(input_df)

        # Convert prediction to float if needed
        prediction_result = float(prediction[0])

        return {"predicted_rent": round(prediction_result, 2)}

    except Exception as e:
        return {"error": str(e)}
