import streamlit as st
import requests

# Define the API endpoint
API_URL = "http://127.0.0.1:8000/predict/"

# Streamlit frontend to input property details
st.title("Rental Price Prediction")
st.write("Enter the details of the property to get a rental price prediction.")

# Inputs
city = st.text_input("City", "Nagpur")
area = st.text_input("Area", "Hulkeshwar")
location = st.text_input("Location", "Hulkeshwar, Nagpur, Maharashtra")
zone = st.text_input("Zone", "South Zone")
property_type = st.selectbox("Property Type", ["1 BHK Flat", "2 BHK Flat", "3 BHK Flat", "4 BHK Flat"])
size_in_sqft = st.number_input("Size in Sqft", min_value=100, value=1000)
bedrooms = st.number_input("Bedrooms", min_value=1, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
balcony = st.number_input("Balcony", min_value=0, value=1)
furnishing_status = st.selectbox("Furnishing Status", ["Unfurnished", "Semi-Furnished", "Fully Furnished"])
number_of_amenities = st.number_input("Number of Amenities", min_value=0, value=2)

# Button to submit data and get prediction
if st.button("Predict Rent"):
    # Prepare the payload
    payload = {
        "city": city,
        "area": area,
        "location": location,
        "zone": zone,
        "property_type": property_type,
        "size_in_sqft": size_in_sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "balcony": balcony,
        "furnishing_status": furnishing_status,
        "number_of_amenities": number_of_amenities
    }

    # Make a POST request to the FastAPI backend
    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        predicted_rent = response.json()["predicted_rent"]
        st.write(f"Predicted Rent: ₹{predicted_rent}")
    else:
        st.write("Error: Could not get prediction.")
