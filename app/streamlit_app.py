import streamlit as st
import requests

# Collect user inputs through Streamlit widgets
city = st.text_input('City', 'Nagpur')
area = st.text_input('Area', 'hulkeshwar')
location = st.text_input('Location', 'hulkeshwar, Nagpur, Maharashtra')
zone = st.selectbox('Zone', ['north', 'south', 'east', 'west'])
property_type = st.selectbox('Property Type', ['1 RK', '1 BHK Flat', '2 BHK Flat', '3 BHK Flat', '2 BHK House', '3 BHK Independent Floor', '1 BHK House', 'Studio Apartment', 'Independent Apartment'])
size_in_sqft = st.number_input('Size (sqft)', min_value=0, max_value=4000, value=1000)
bedrooms = st.number_input('Number of Bedrooms', min_value=0, max_value=5, value=2)
bathrooms = st.number_input('Number of Bathrooms', min_value=0, max_value=4, value=2)
balcony = st.number_input('Number of Balconies', min_value=0, max_value=4, value=2)
furnishing_status = st.selectbox('Furnishing Status', ['unfurnished', 'semi-furnished', 'furnished'])
number_of_amenities = st.number_input('Number of Amenities', min_value=0, max_value=10, value=2)

# Form the input data as a dictionary
input_data = {
    'city': city,
    'area': area,
    'location': location,
    'zone': zone,
    'property_type': property_type,
    'size_in_sqft': size_in_sqft,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'balcony': balcony,
    'furnishing_status': furnishing_status,
    'number_of_amenities': number_of_amenities
}

# Streamlit app will call the FastAPI endpoint for predictions
if st.button('Get Predicted Rent'):
    fastapi_url = "https://rental-price-fastapi.onrender.com/predict"  # Update with your FastAPI URL
    response = requests.post(fastapi_url, json=input_data)

    if response.status_code == 200:
        predicted_rent = response.json()["predicted_rent"]
        st.write(f"Predicted Rent: ₹{predicted_rent}")
    else:
        st.write("Error getting prediction")
