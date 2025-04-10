from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import RentalInput
import pickle
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your model
with open("app/model/best_linear_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def root():
    return {"message": "Rental Price Prediction API is Live!"}

@app.post("/predict")
def predict_price(data: RentalInput):
    # Prepare input data correctly (assuming one-hot encoded or numerical model)
    input_array = np.array([[  # adjust as needed
        data.city, data.area, data.location, data.zone, data.property_type,
        data.size_in_sqft, data.bedrooms, data.bathrooms, data.balcony,
        data.furnishing_status, data.Number_of_amenities, data.security_deposite,
        data.property_age, data.brokerage, data.floor_no, data.maintenance_charge,
        data.nearby_facilities, data.type_of_society, data.road_connectivity
    ]])

    prediction = model.predict(input_array)[0]
    return {"predicted_price": prediction}
