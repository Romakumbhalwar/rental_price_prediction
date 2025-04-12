import streamlit as st
import requests

st.title("🏠 Rental Price Prediction")
st.markdown("Select property details to predict the rent.")

# Dropdown options
cities = ['Nagpur']  
areas = ['manewada', 'hudkeswar', 'besa', 'sitabuldi', 'hingna', 'wardha road', 'pratap nagar', 'mhalgi nagar']
locations = ['Manewada, Nagpur, Maharashtra', 'Hingna, Nagpur', 'Sitabuldi, Nagpur', 'Hudkeshwar Road, Nagpur']
zones = ['south zone', 'east zone', 'rural', 'north zone', 'west zone', 'central zone']
property_types = ['1 BHK Flat', '2 BHK Flat', '3 BHK Flat', '1 RK', '2 BHK house', '1 BHK house']
furnishing_statuses = ['Unfurnished', 'Semi Furnished', 'Fully Furnished']
brokerage_options = ['No', 'Yes']
maintenance_charge_options = ['No', 'Yes']
nearby_facilities_options = ['school', 'hospital', 'metro station', 'airport', 'bus stop']
type_of_society_options = ['Gated', 'Non-Gated', 'Township']
road_connectivity_options = ['under 500 m', 'under 1 km', 'under 2 km', 'under 5 km']

with st.form("rental_form"):
    city = st.selectbox("City", cities)  
    area = st.selectbox("Area", areas)
    location = st.selectbox("Location", locations)
    zone = st.selectbox("Zone", zones)
    property_type = st.selectbox("Property Type", property_types)
    
    size_in_sqft = st.number_input("Size (sqft)", min_value=100, max_value=10000, value=800)
    bedrooms = st.slider("Bedrooms", 1, 5, 2)
    bathrooms = st.slider("Bathrooms", 1, 5, 2)
    balcony = st.slider("Balcony", 0, 3, 1)
    
    furnishing_status = st.selectbox("Furnishing Status", furnishing_statuses)
    Number_of_amenities = st.slider("Number of Amenities", 0, 10, 3)
    security_deposite = st.number_input("Security Deposit", value=10000)
    property_age = st.slider("Property Age (Years)", 0, 30, 5)
    brokerage = st.selectbox("Brokerage", brokerage_options)
    floor_no = st.number_input("Floor No.", min_value=0, max_value=20, value=2)
    maintenance_charge = st.selectbox("Maintenance Charge", maintenance_charge_options)
    nearby_facilities = st.selectbox("Nearby Facilities", nearby_facilities_options)
    type_of_society = st.selectbox("Type of Society", type_of_society_options)
    road_connectivity = st.selectbox("Road Connectivity", road_connectivity_options)

    submit = st.form_submit_button("Predict Rent 💰")

if submit:
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
        "Number_of_amenities": Number_of_amenities,
        "security_deposite": security_deposite,
        "property_age": property_age,
        "brokerage": brokerage,
        "floor_no": floor_no,
        "maintenance_charge": maintenance_charge,
        "nearby_facilities": nearby_facilities,
        "type_of_society": type_of_society,
        "road_connectivity": road_connectivity
    }

    requests.post("https://rental-fastapi.onrender.com/predict", json=input_data)
    if response.status_code == 200:
        result = response.json()
        if "predicted_price" in result:
            prediction = result["predicted_price"]
            st.success(f"🏡 Predicted Rent: ₹ {prediction}")
        else:
            st.error("⚠️ Response received, but 'predicted_price' not found.")
    else:
        st.error("❌ Failed to get prediction from the server.")
