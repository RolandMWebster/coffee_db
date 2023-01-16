import folium
from folium.plugins import MarkerCluster

from coffee_db.coffee import Coffee, Country


class MapVisualizer:
    def plot_coffees_by_country(self, coffees: list[Coffee]) -> folium.Map:
        """
        PLots a world map with cluster points for coffee counts by country.
        """
        world_map = folium.Map(tiles="cartodbpositron")
        marker_cluster = MarkerCluster().add_to(world_map)

        coffee_counts_by_country = get_coffees_by_country(coffees)
        for country_name, coffee_count in coffee_counts_by_country.items():
            country = Country(id=1, name=country_name)
            lat, long = country.get_lat_long()
            popup_text = self._get_popup_text(country.name, coffee_count)
            folium.CircleMarker(
                    location=[lat, long],
                    radius=coffee_count,
                    popup=popup_text,
                    fill=True
                ).add_to(marker_cluster)
        return world_map

    def _get_popup_text(self, country_name: str, num_coffees: int) -> str:
        return (
            f"Country: {country_name}<br>"
            f"Coffees: {num_coffees}"
        )


# TODO: Find a new home for get_coffees_by_country / refactor
def get_coffees_by_country(coffees: list[Coffee]) -> dict[Country, int]:
    """
    Returns a dictionary of counts of coffees by country.
    """
    coffee_counts_by_country = {}
    for coffee in coffees:
        country = coffee.country_of_origin.name
        if country in coffee_counts_by_country:
            coffee_counts_by_country[country] += 1
        else:
            coffee_counts_by_country[country] = 1
    return coffee_counts_by_country


if __name__ == "__main__":
    from coffee_db.coffee import Roastery
    visualizer = MapVisualizer()

    # make some countries
    kenya = Country(id=1, name="Kenya")
    mexico = Country(id=2, name="Mexico")
    us = Country(id=3, name="US")

    # make a roastery
    heart = Roastery(id=1, name="Heart Coffee", country=us)

    # make some coffees
    coffee1 = Coffee(
        id=1,
        name="Kenya AA",
        country_of_origin=kenya,
        roastery=heart,
        elevation=1800
    )
    coffee2 = Coffee(
        id=2,
        name="Kenya BB",
        country_of_origin=kenya,
        roastery=heart,
        elevation=1700
    )
    visualizer.plot_coffees_by_country([coffee1, coffee2])