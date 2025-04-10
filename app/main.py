from fastapi import FastAPI
from app.schemas import RentalInput
import pickle
import numpy as np

app = FastAPI()

# Load your model
with open("app/model/best_linear_model.pkl", "rb") as f:
    model = pickle.load(f)

# Function to encode categorical inputs
def encode_input(data):
    enc = {
        "furnishing_status": {"Unfurnished": 0, "Semi Furnished": 1, "Fully Furnished": 2},
        "brokerage": {"No": 0, "Yes": 1},
        "maintenance_charge": {"No": 0, "Yes": 1},
        "type_of_society": {"Gated": 0, "Non-Gated": 1, "Township": 2},
        "road_connectivity": {
            "under 500 m": 0, "under 1 km": 1, "under 2 km": 2, "under 5 km": 3
        },
        "city": {"Nagpur": 0},
        "area": {
            "manewada": 0, "hudkeswar": 1, "besa": 2, "sitabuldi": 3,
            "hingna": 4, "wardha road": 5, "pratap nagar": 6, "mhalgi nagar": 7
        },
        "location": {
            "Manewada, Nagpur, Maharashtra": 0,
            "Hingna, Nagpur": 1,
            "Sitabuldi, Nagpur": 2,
            "Hudkeshwar Road, Nagpur": 3
        },
        "zone": {
            "south zone": 0, "east zone": 1, "rural": 2,
            "north zone": 3, "west zone": 4, "central zone": 5
        },
        "property_type": {
            "1 BHK Flat": 0, "2 BHK Flat": 1, "3 BHK Flat": 2,
            "1 RK": 3, "2 BHK house": 4, "1 BHK house": 5
        },
        "nearby_facilities": {
            "school": 0, "hospital": 1, "metro station": 2,
            "airport": 3, "bus stop": 4
        }
    }

    data = data.copy()
    for key, mapping in enc.items():
        if key in data:
            data[key] = mapping.get(data[key], 0)  # default to 0 if not found
    return data

@app.get("/")
def root():
    return {"message": "Rental Price Prediction API is Live!"}

@app.post("/predict")
def predict_price(data: RentalInput):
    input_dict = data.dict()
    encoded = encode_input(input_dict)

    input_array = np.array([list(encoded.values())], dtype=float)
    prediction = model.predict(input_array)[0]
    return {"predicted_price": prediction}
