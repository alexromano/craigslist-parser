from enum import Enum
from typing import Optional, List, Literal
from pydantic import BaseModel

class Categories(Enum):
    APARTMENT = "apa"
    SUBLET_TMP = "sub"
    ROOM = "roo"

class Neighborhoods(Enum):
    SOMA = "SOMA / south beach"
    USF = "USF / panhandle"
    BERNAL_HEIGHTS = "bernal heights"
    CASTRO = "castro / upper market"
    COLE_VALLEY = "cole valley / ashbury hts"
    DOWNTOWN = "downtown / civic / van ness"
    GLEN_PARK = "glen park"
    LOWER_HAIGHT = "lower haight"
    HAIGHT_ASHBURY = "haight ashbury"
    HAYES_VALE = "hayes valley"
    INNER_RICHMOND = "inner richmond"
    INNER_SUNSET = "inner sunset / UCSF"
    NOE_VALLEY = "noe valley"
    NOPA = "alamo square / nopa"

class Laundry(Enum):
    IN_UNIT = 1
    IN_BUILDING = 2
    ON_SITE = 3
    HOOKUPS = 4
    NONE = 5

class LeasePeriod(BaseModel):
    unit: Literal["monthly", "yearly"]
    duration: Optional[str]

class DatesAvailable(BaseModel):
    start_date: str
    end_date: Optional[str]

class ApplicationFee(BaseModel):
    amount: int

class Parking(BaseModel):
    available: bool
    amount: Optional[int]

class RoommateInfo(BaseModel):
    age: Optional[int] = None
    occupation: Optional[str] = None
    description: str

class Roommates(BaseModel):
    amount: Optional[int]
    roommates: Optional[List[RoommateInfo]] = None

class Bedrooms(BaseModel):
    amount: int
    bathrooms: int

class Furnished(BaseModel):
    is_furnished: bool
    description: str
