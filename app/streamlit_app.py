import streamlit as st
import requests

# Collect user inputs through Streamlit widgets
city = st.text_input('City', 'Nagpur')
area = st.text_input('Area', 'hulkeshwar')
location = st.text_input('Location', 'hulkeshwar, Nagpur, Maharashtra')
zone = st.text_input('Zone', 'south zone')
property_type = st.selectbox('Property Type', ['1 BHK Flat', '2 BHK Flat', '3 BHK Flat'])
size_in_sqft = st.number_input('Size (sqft)', min_value=0, value=1000)
bedrooms = st.number_input('Number of Bedrooms', min_value=0, value=2)
bathrooms = st.number_input('Number of Bathrooms', min_value=0, value=2)
balcony = st.number_input('Number of Balconies', min_value=0, value=2)
furnishing_status = st.selectbox('Furnishing Status', ['unfurnished', 'semi-furnished', 'furnished'])
number_of_amenities = st.number_input('Number of Amenities', min_value=0, value=2)

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
    fastapi_url = "https://your-fastapi-url.onrender.com/predict"  # Update with your FastAPI URL
    response = requests.post(fastapi_url, json=input_data)
    if response.status_code == 200:
        predicted_rent = response.json()["predicted_rent"]
        st.write(f"Predicted Rent: ₹{predicted_rent}")
    else:
        st.write("Error getting prediction")
