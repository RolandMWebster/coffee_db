import datetime
from typing import List, Optional

from pydantic import BaseModel, validator
from geopy.geocoders import Nominatim


class BaseCoffeeDbObject(BaseModel):
    id: int
    name: str

    @validator("name")
    def name_must_be_capitalized(cls, v):
        if not v[0].isupper():
            raise ValueError("name must be capitalized")
        return v

    def __str__(self):
        return self.name


class Continent(BaseCoffeeDbObject):
    pass


class Country(BaseCoffeeDbObject):
    continent: Optional[Continent] = None

    def get_lat_long(self) -> tuple[int, int]:
        """
        Returns the lat long position of the country's centroid.
        """
        geolocator = Nominatim(user_agent="coffee_db")
        loc = geolocator.geocode(self.name)
        return (loc.latitude, loc.longitude)


class Roastery(BaseCoffeeDbObject):
    country: Country


class Variety(BaseCoffeeDbObject):
    pass


class Process(BaseCoffeeDbObject):
    pass


class CoffeeUser(BaseCoffeeDbObject):
    pass


class Coffee(BaseCoffeeDbObject):
    date_added: datetime.datetime
    added_by: CoffeeUser
    country_of_origin: Country
    roastery: Roastery
    process: Process
    varietal: List[Variety]
    elevation: Optional[int] = None
    tasting_notes: Optional[str] = None

    @validator("elevation")
    def name_must_be_capitalized(cls, v):
        if v:
            if v <= 0:
                raise ValueError("elevation must be greater than zero")
        return v

    @validator("tasting_notes")
    def tasting_notes_must_be_lower_case(cls, v):
        if not v.islower():
            raise ValueError("tasting notes must be comma separated, and lower case")
