from pydantic import BaseModel

class RentPredictionRequest(BaseModel):
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
    number_of_amenities: int
