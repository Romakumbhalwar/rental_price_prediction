import streamlit as st
import requests

st.title("🏠 Rental Price Prediction App")

# Collect user inputs through Streamlit widgets
city = st.text_input('City', 'Nagpur')
area = st.text_input('Area', 'hulkeshwar')
location = st.text_input('Location', 'hulkeshwar, Nagpur, Maharashtra')
zone = st.selectbox('Zone', ['east', 'west', 'north', 'south'])
property_type = st.selectbox('Property Type', [
    '1 RK', '1 BHK Flat', '2 BHK Flat', '3 BHK Flat',
    '2 BHK House', '3 BHK Independent Floor', '1 BHK House',
    'Studio Apartment', 'Independent Apartment'
])
size_in_sqft = st.slider('Size (in sqft)', 0, 4000, 1000)
bedrooms = st.slider('Number of Bedrooms', 0, 5, 2)
bathrooms = st.slider('Number of Bathrooms', 0, 4, 2)
balcony = st.slider('Number of Balconies', 0, 4, 2)
furnishing_status = st.selectbox('Furnishing Status', ['unfurnished', 'semi-furnished', 'furnished'])
number_of_amenities = st.slider('Number of Amenities', 0, 10, 3)

# Create input JSON
input_data = {
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

if st.button("Predict Rent"):
    with st.spinner("Sending data to prediction API..."):
        try:
            response = requests.post("https://rental-price-fastapi.onrender.com/predict", json=input_data)
            result = response.json()
            if "predicted_rent" in result:
                st.success(f"💸 Estimated Rent: ₹{result['predicted_rent']}")
            else:
                st.error(f"Error: {result.get('error', 'Unknown error occurred')}")
        except Exception as e:
            st.error(f"Failed to fetch prediction: {e}")
