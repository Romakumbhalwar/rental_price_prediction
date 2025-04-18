from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class InputData(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    property_type: str
    size_in_sqft: float
    bedrooms: int
    bathrooms: int
    balcony: int
    furnishing_status: str
    number_of_amenities: int

# ✅ Load model at startup
try:
    model_dict = joblib.load("app/model/best_rent_model.pkl")
    model = model_dict["model"]
    features = model_dict["features"]
    print("✅ Model loaded successfully:", type(model))
except Exception as e:
    print("❌ Error loading model:", e)

@app.post("/predict")
def predict_rent(data: InputData):
    try:
        input_data = [[
            data.city,
            data.area,
            data.location,
            data.zone,
            data.property_type,
            data.size_in_sqft,
            data.bedrooms,
            data.bathrooms,
            data.balcony,
            data.furnishing_status,
            data.number_of_amenities
        ]]
        prediction = model.predict(input_data)
        return {"predicted_rent": round(prediction[0], 2)}
    except Exception as e:
        return {"error": str(e)}
