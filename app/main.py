from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import RentalInput
import pickle
import numpy as np

app = FastAPI()

# Enable CORS
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

# Example encodings (make sure they match how your model was trained)
label_map = {
    'Nagpur': 0,
    'manewada': 1,
    'manewada,nagpur': 2,
    'south zone': 3,
    '1 BHK Flat': 4,
    'Semi Furnished': 5,
    'No': 0,
    'Yes': 1,
    'school': 6,
    'Gated': 7,
    'under 1 km': 8,
    # Add other required mappings from your training
}

def encode(value):
    return label_map.get(value, -1)  # fallback to -1 if not found

@app.get("/")
def root():
    return {"message": "Rental Price Prediction API is Live!"}

@app.post("/predict")
def predict_price(data: RentalInput):
    try:
        input_array = np.array([[
            encode(data.city),
            encode(data.area),
            encode(data.location),
            encode(data.zone),
            encode(data.property_type),
            data.size_in_sqft,
            data.bedrooms,
            data.bathrooms,
            data.balcony,
            encode(data.furnishing_status),
            data.Number_of_amenities,
            data.security_deposite,
            data.property_age,
            encode(data.brokerage),
            data.floor_no,
            encode(data.maintenance_charge),
            encode(data.nearby_facilities),
            encode(data.type_of_society),
            encode(data.road_connectivity)
        ]])

        prediction = model.predict(input_array)[0]
        return {"predicted_price": prediction}
    except Exception as e:
        return {"error": str(e)}
