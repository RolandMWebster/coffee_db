import datetime
from typing import List, Optional

from pydantic import BaseModel, validator
from geopy.geocoders import Nominatim


def check_name(name: str):
    if len(name) == 0:
        raise ValueError("Please provide a Name")
    elif not name[0].isupper():
        raise ValueError("Name must be capitalized")
    else:
        return name


def name_must_be_capitalized(name: str):
    if name[0].isupper():
        return name
    else:
        raise ValueError("Name must be capitalized")


def tasting_notes_must_be_lower_case(tasting_notes: str):
    if tasting_notes:
        if not tasting_notes.islower():
            raise ValueError("tasting notes must be comma separated, and lower case")
    return tasting_notes


def elevation_must_be_greater_than_zero(elevation: int):
    if elevation:
        if elevation <= 0:
            raise ValueError("elevation must be greater than zero")
    return elevation


class BaseCoffeeDbObject(BaseModel):
    id: int
    name: str

    # validators
    _check_name = validator('name', allow_reuse=True)(check_name)

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

    # validators
    _check_tasting_notes = validator('tasting_notes', allow_reuse=True)(tasting_notes_must_be_lower_case)
    _check_elevation = validator('elevation', allow_reuse=True)(elevation_must_be_greater_than_zero)
