import datetime
from typing import List, Optional
from pydantic import BaseModel
from geopy.geocoders import Nominatim


class Continent(BaseModel):
    id: int
    name: str


class Country(BaseModel):
    id: int
    name: str
    continent: Optional[Continent] = None

    def get_lat_long(self) -> tuple[int, int]:
        """
        Returns the lat long position of the country's centroid.
        """
        geolocator = Nominatim(user_agent="coffee_db")
        loc = geolocator.geocode(self.name)
        return (loc.latitude, loc.longitude)

    def __str__(self):
        return self.name


class Roastery(BaseModel):
    id: int
    name: str
    country: Country

    def __str__(self):
        return self.name


class Variety(BaseModel):
    id: int
    name: str

    def __str__(self):
        return self.name


class Process(BaseModel):
    id: int
    name: str

    def __str__(self):
        return self.name


class CoffeeUser(BaseModel):
    id: int
    name: str

    def __str__(self):
        return self.name


class Coffee(BaseModel):
    id: int
    date_added: datetime.datetime
    added_by: CoffeeUser
    name: str
    country_of_origin: Country
    roastery: Roastery
    process: Process
    varietal: List[Variety]
    elevation: Optional[int] = None
    tasting_notes: Optional[str] = None

    def __str__(self):
        return self.name
