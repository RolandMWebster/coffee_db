import copy

from coffee_db.coffee import Country, Roastery, Coffee, Process, CoffeeUser, Variety
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

    def _get_varieties(self) -> dict[str, Variety]:
        """
        Builds Variety pydantic models from the db data.
        """
        varieties = self.db.get_data("variety")
        varieties_dict: dict[str, Variety] = {}
        for variety in varieties:
            varieties_dict[variety["name"]] = Variety(**variety)
        return varieties_dict

    def _get_processes(self) -> dict[str, Process]:
        """
        Builds Process pydantic models from the db data.
        """
        processes = self.db.get_data("process")
        processes_dict: dict[str, Process] = {}
        for process in processes:
            processes_dict[process["name"]] = Process(**process)
        return processes_dict
    
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

    def _get_coffee_users(self) -> dict[str, Variety]:
        """
        Builds CoffeeUser pydantic models from the db data.
        """
        coffee_users = self.db.get_data("coffee_user")
        coffee_users_dict: dict[str, CoffeeUser] = {}
        for coffee_user in coffee_users:
            coffee_users_dict[coffee_user["name"]] = CoffeeUser(**coffee_user)
        return coffee_users_dict

    def _get_coffees(
        self,
        countries: dict[str, Country],
        roasteries: dict[str, Roastery],
        varieties: dict[str, Variety],
        processes: dict[str, Process],
        coffee_users: dict[str, CoffeeUser],
    ) -> dict[str, Coffee]:
        """
        Builds Coffee pydantic models from the db data.
        """
        coffees = self.db.get_data("coffee")
        coffees_dict: dict[str, Coffee] = {}
        coffees_copy = copy.deepcopy(coffees)
        for coffee in coffees_copy:
            for coffee_attr in [
                ("roastery", roasteries),
                ("country_of_origin", countries),
                ("varietal", varieties),
                ("process", processes),
                ("added_by", coffee_users),
            ]:
                try:
                    coffee[coffee_attr[0]] = coffee_attr[1][coffee[coffee_attr[0]]]
                except KeyError:
                    raise KeyError(
                        f"Coffee {coffee['name']} is from unknown {coffee_attr[0]} {coffee[coffee_attr[0]]}."
                        f"Ensure {coffee[coffee_attr[0]]} is in the {coffee_attr[0]} table."
                    )
            coffees_dict[coffee["name"]] = Coffee(**coffee)
        return coffees_dict

    def get_data(self) -> tuple[list[Country], list[Roastery], list[Coffee]]:
        """
        Returns pydantic data models for Coffees, Roasteries, Countries, Process and Varieties.
        """
        countries = self._get_countries()
        processes = self._get_processes()
        coffee_users = self._get_coffee_users()
        varieties = self._get_varieties()
        roasteries = self._get_roasteries(countries)
        coffees = self._get_coffees(countries, roasteries, varieties, processes, coffee_users)
        return (
            list(countries.values()),
            list(roasteries.values()),
            list(coffees.values()),
            list(processes.values()),
            list(varieties.values()),
            list(coffee_users.values())
        )
