import copy

from coffee_db.coffee import Country, Roastery, Coffee
from coffee_db import CoffeeDB


class PostgresDataLoader:
    """
    Class for loading data from SQL into Pydantic data models.
    """
    def __init__(self, db: CoffeeDB):
        self.db = db

    def _get_countries(self) -> dict[str, Country]:
        """
        Builds Country pydantic models from the db data.
        """
        countries = self.db.get_data("country")
        countries_dict: dict[str, Country] = {}
        for country in countries:
            countries_dict[country["name"]] = Country(**country)
        return countries_dict
    
    def _get_roasteries(self, countries: dict[str, Country]) -> dict[str, Roastery]:
        """
        Builds Roastery pydantic models from the db data.
        """
        roasteries = self.db.get_data("roastery")
        roasteries_dict: dict[str, Roastery] = {}
        roasteries_copy = copy.deepcopy(roasteries)
        for roastery in roasteries_copy:
            try:
                roastery["country"] = countries[roastery["country"]]
            except KeyError:
                raise KeyError(
                    f"Roastery {roastery['name']} is from unknown country {roastery['country']}. "
                    f"Ensure {roastery['country']} is in the country table."
                )
            roasteries_dict[roastery["name"]] = Roastery(**roastery)
        return roasteries_dict

    def _get_coffees(
        self, countries: dict[str, Country], roasteries: dict[str, Roastery]
    ) -> dict[str, Coffee]:
        """
        Builds Coffee pydantic models from the db data.
        """
        coffees = self.db.get_data("coffee")
        coffees_dict: dict[str, Coffee] = {}
        coffees_copy = copy.deepcopy(coffees)
        for coffee in coffees_copy:
            try:
                coffee["roastery"] = roasteries[coffee["roastery"]]
            except KeyError:
                raise KeyError(
                    f"Coffee {coffee['name']} is from unknown roastery {coffee['roastery']}."
                    f"Ensure {coffee['roastery']} is in the roastery table."
                )
            try:
                coffee["country_of_origin"] = countries[coffee["country_of_origin"]]
            except KeyError:
                raise KeyError(
                    f"Coffee {coffee['name']} is from unknown country {coffee['country']}."
                    f"Ensure {coffee['country']} is in the country table."
                )
            coffees_dict[coffee["name"]] = Coffee(**coffee)
        return coffees_dict

    def get_data(self) -> tuple[list[Country], list[Roastery], list[Coffee]]:
        """
        Returns pydantic data models for Coffees, Roasteries, and Countries.
        """
        countries = self._get_countries()
        roasteries = self._get_roasteries(countries)
        coffees = self._get_coffees(countries, roasteries)
        return (list(countries.values()), list(roasteries.values()), list(coffees.values()))
