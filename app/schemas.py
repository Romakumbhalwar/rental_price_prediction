from pydantic import BaseModel

class RentInput(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    property_type: str
    lease_type: str
    furnishing: str
    tenant_preferred: str
    bathroom: int
    floor: int
    total_floor: int
    carpet_area: float
    size_in_sqft: float
    age_of_property: int
    gated_security: int
    amenities: int
    brokerage: float
    maintenance: float
    security_deposit: float
