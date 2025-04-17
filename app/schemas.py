from pydantic import BaseModel

class PropertyData(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    property_type: str
    size_in_sqft: int
    bedrooms: int
    bathrooms: int
    balcony: int
    furnishing_status: str
    number_of_amenities: int
