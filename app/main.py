from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import RentalInput
import joblib
import numpy as np

app = FastAPI()

# Allow CORS (important if your Streamlit app is hosted separately)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your Streamlit app domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and encoders
model = joblib.load("app/model/best_linear_model.pkl")
encoders = joblib.load("app/model/encoders.pkl")

@app.get("/")
def root():
    return {"message": "Rental Price Prediction API is Live!"}

@app.post("/predict")
def predict_price(data: RentalInput):
    input_dict = data.dict()

    # Encode categorical features
    for col in encoders:
        if col in input_dict:
            value = str(input_dict[col])
            if value in encoders[col].classes_:
                input_dict[col] = encoders[col].transform([value])[0]
            else:
                raise ValueError(f"'{value}' not found in encoder for column '{col}'")

    # Convert to array and predict
    input_array = np.array([list(input_dict.values())])
    prediction = model.predict(input_array)[0]

    return {"predicted_price": round(prediction, 2)}
