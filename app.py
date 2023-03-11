import streamlit as st
from streamlit_folium import folium_static

from coffee_db import CoffeeDB
from coffee_db.validate import InputValidator
from coffee_db.data_loaders import PostgresDataLoader
from coffee_db.visualizations.world_map_visualizer import MapVisualizer
from coffee_db.streamlit_utils import forms


def main():

    st.title("Hello Coffee World!")

    folium_static(plot_map())

    show_tables()

    add_forms()
    remove_forms()


def show_tables():

    option = st.selectbox("Show Table", options=["none", "coffee", "roastery", "country"])

    if option == "none":
        pass
    else:
        data = db.get_data(option)
        st.dataframe(data)


def add_forms():
    with st.expander("Add Entry"):
        add_coffee_form()
        add_roastery_form()
        add_country_form()
        add_process_form()
        add_variety_form()


def remove_forms():
    with st.expander("Delete Entry"):
        remove_coffee_form()
        remove_roastery_form()
        remove_country_form()
        remove_process_form()
        remove_variety_form()


def add_coffee_form():
    coffee_form = forms.CoffeeForm()
    coffee_form.add_entry_form(
        coffee_users=coffee_users,
        countries=countries,
        roasteries=roasteries,
        processes=processes,
        varieties=varieties,
        )


def remove_coffee_form():
    coffee_form = forms.CoffeeForm()
    coffee_form.remove_entry_form()


def add_roastery_form():
    roastery_form = forms.RoasteryForm()
    roastery_form.add_entry_form(countries=countries)


def remove_roastery_form():
    roastery_form = forms.RoasteryForm()
    roastery_form.remove_entry_form()


def add_country_form():
    country_form = forms.CountryForm()
    country_form.add_entry_form()


def remove_country_form():
    country_form = forms.CountryForm()
    country_form.remove_entry_form()


def add_process_form():
    process_form = forms.ProcessForm()
    process_form.add_entry_form()


def remove_process_form():
    process_form = forms.ProcessForm()
    process_form.remove_entry_form()


def add_variety_form():
    variety_form = forms.VarietyForm()
    variety_form.add_entry_form()


def remove_variety_form():
    variety_form = forms.VarietyForm()
    variety_form.remove_entry_form()


def plot_map():

    visualizer = MapVisualizer()
    return visualizer.plot_coffees_by_country(coffees)


if __name__ == "__main__":

    db = CoffeeDB()
    data_loader = PostgresDataLoader(db=db)

    countries, roasteries, coffees, processes, varieties, coffee_users = data_loader.get_data()

    input_validator = InputValidator()

    main()
