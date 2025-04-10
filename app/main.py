from fastapi import FastAPI
from app.schemas import RentalInput
import pickle

with open("app/model/best_linear_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Encodings

city_encoding = {
    'Nagpur': 0
}

area_encoding = {
    'manewada': 0, 'hudkeswar': 1, 'besa': 2, 'sitabuldi': 3, 'hingna': 4,
    'wardha road': 5, 'pratap nagar': 6, 'mhalgi nagar': 7
}
location_encoding = {
    'Manewada, Nagpur, Maharashtra': 0, 'Hingna, Nagpur': 1,
    'Sitabuldi, Nagpur': 2, 'Hudkeshwar Road, Nagpur': 3
}
zone_encoding = {
    'south zone': 0, 'east zone': 1, 'rural': 2,
    'north zone': 3, 'west zone': 4, 'central zone': 5
}
property_type_encoding = {
    '1 BHK Flat': 0, '2 BHK Flat': 1, '3 BHK Flat': 2,
    '1 RK': 3, '2 BHK house': 4, '1 BHK house': 5
}
furnishing_status_encoding = {
    'Unfurnished': 0, 'Semi Furnished': 1, 'Fully Furnished': 2
}
brokerage_encoding = {'No': 0, 'Yes': 1}
maintenance_charge_encoding = {'No': 0, 'Yes': 1}
nearby_facilities_encoding = {
    'school': 0, 'hospital': 1, 'metro station': 2,
    'airport': 3, 'bus stop': 4
}
type_of_society_encoding = {'Gated': 0, 'Non-Gated': 1, 'Township': 2}
road_connectivity_encoding = {
    'under 500 m': 0, 'under 1 km': 1, 'under 2 km': 2, 'under 5 km': 3
}

@app.post("/predict")
def predict_price(data: RentalInput):
    try:
        model_input = [
            city_encoding.get(data.city, 0),
            data.size_in_sqft,
            data.bedrooms,
            data.bathrooms,
            data.balcony,
            area_encoding.get(data.area, 0),
            location_encoding.get(data.location, 0),
            zone_encoding.get(data.zone, 0),
            property_type_encoding.get(data.property_type, 0),
            furnishing_status_encoding.get(data.furnishing_status, 0),
            data.Number_of_amenities,
            data.security_deposite,
            data.property_age,
            brokerage_encoding.get(data.brokerage, 0),
            data.floor_no,
            maintenance_charge_encoding.get(data.maintenance_charge, 0),
            nearby_facilities_encoding.get(data.nearby_facilities, 0),
            type_of_society_encoding.get(data.type_of_society, 0),
            road_connectivity_encoding.get(data.road_connectivity, 0)
        ]

        prediction = model.predict([model_input])[0]
        return {"predicted_price": round(prediction, 2)}
    except Exception as e:
        return {"error": str(e)}
