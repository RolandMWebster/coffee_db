import streamlit as st
from streamlit_folium import folium_static

from coffee_db import CoffeeDB
from coffee_db.data_loaders import PostgresDataLoader
from coffee_db.app.utils import Page, Tab
from coffee_db.visualizations.world_map_visualizer import MapVisualizer


class HomePage(Page):

    NAME = "Home Page"

    def __init__(self, tabs: list[Tab] = None):
        self.tabs = tabs
        self.visualizer = MapVisualizer()


    def write(self):
        st.title(self.NAME)

        db = CoffeeDB()
        data_loader = PostgresDataLoader(db=db)
        countries, roasteries, coffees = data_loader.get_data()
        folium_static(self.visualizer.plot_coffees_by_country(coffees))
        self.write_tabs()
