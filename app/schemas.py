from pydantic import BaseModel

class RentalInput(BaseModel):
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
    Number_of_amenities: int
    security_deposite: float
    property_age: int
    brokerage: str
    floor_no: int
    maintenance_charge: str
    nearby_facilities: str
    type_of_society: str
    road_connectivity: str
