import copy

import streamlit as st
from streamlit_folium import st_folium

from coffee_db import CoffeeDB
from coffee_db.coffee import Coffee, Roastery, Country
from coffee_db.visualizations.world_map_visualizer import MapVisualizer


def main():

    # Title and Overview of Data
    st.title("Hello Coffee World!")

    st_folium(plot_map())

    st.dataframe(coffees)
    st.dataframe(roasteries)
    st.dataframe(countries)

    add_forms()
    remove_forms()


def add_forms():

    col1, col2, col3 = st.columns(3)

    with col1:
        add_coffee_form()
    with col2:
        add_roastery_form()
    with col3:
        add_country_form()


def remove_forms():

    col1, col2, col3 = st.columns(3)

    with col1:
        remove_coffee_form()
    with col2:
        remove_roastery_form()
    with col3:
        remove_country_form()


def add_coffee_form():
    st.header("Add Coffee")
    with st.form(key="add_coffee", clear_on_submit=True):
        name = st.text_input("Name")
        country_of_origin = st.selectbox(
            "Country of Origin", (x["name"] for x in countries)
        )
        roastery = st.selectbox(
            "Roastery", (x["name"] for x in roasteries)
        )
        elevation = st.text_input("Elevation")
        submit = st.form_submit_button("Add")
        if submit:
            db.insert_row(
                "coffee",
                (
                    name,
                    country_of_origin,
                    roastery,
                    elevation,
                ),
            )
            st.experimental_rerun()


def remove_coffee_form():
    st.header("Remove Coffee")
    with st.form(key="remove_coffee", clear_on_submit=True):
        coffee_id = st.text_input("ID")
        submit = st.form_submit_button("Remove")
        if submit:
            db.remove_row(
                "coffee", (int(coffee_id),)
            )
            st.experimental_rerun()


def add_roastery_form():
    st.header("Add Roastery")
    with st.form(key="add_roastery", clear_on_submit=True):
        name = st.text_input("Name")
        country = st.selectbox(
            "Country", (x["name"] for x in countries)
        )
        submit = st.form_submit_button("Add")
        if submit:
            db.insert_row(
                "roastery",
                (
                    name,
                    country,
                ),
            )
            st.experimental_rerun()


def remove_roastery_form():
    st.header("Remove Roastery")
    with st.form(key="remove_roastery", clear_on_submit=True):
        roastery_id = st.text_input("ID")
        submit = st.form_submit_button("Remove")
        if submit:
            db.remove_row(
                "roastery", (int(roastery_id),)
            )
            st.experimental_rerun()


def add_country_form():
    st.header("Add Country")
    with st.form(key="add_country", clear_on_submit=True):
        name = st.text_input("Name")
        submit = st.form_submit_button("Add")
        if submit:
            db.insert_row("country", (name,))
            st.experimental_rerun()


def remove_country_form():
    st.header("Remove Country")
    with st.form(key="remove_country", clear_on_submit=True):
        country_id = st.text_input("ID")
        submit = st.form_submit_button("Remove")
        if submit:
            db.remove_row("country", (int(country_id),))
            st.experimental_rerun()


def plot_map():

    visualizer = MapVisualizer()
    
    countries_copy = copy.deepcopy(countries)
    country_dict = {}
    for x in countries_copy:
        country_dict[x["name"]] = Country(**x)
    
    roasteries_copy = copy.deepcopy(roasteries)
    roastery_dict = {}
    for x in roasteries_copy:
        x["country"] = country_dict[x["country"]]
        roastery_dict[x["name"]] = Roastery(**x)
    
    coffees_copy = copy.deepcopy(coffees)
    coffee_dict = {}
    for x in coffees_copy:
        x["roastery"] = roastery_dict[x["roastery"]]
        x["country_of_origin"] = country_dict[x["country_of_origin"]]
        coffee_dict[x["name"]] = Coffee(**x)

    return visualizer.plot_coffees_by_country(list(coffee_dict.values()))


if __name__ == "__main__":

    db = CoffeeDB()

    coffees = db.get_data("coffee")
    roasteries = db.get_data("roastery")
    countries = db.get_data("country")

    main()
