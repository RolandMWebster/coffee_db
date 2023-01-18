
import streamlit as st
from streamlit_folium import folium_static
import pandas as pd

from coffee_db import CoffeeDB
from coffee_db.data_loaders import PostgresDataLoader
from coffee_db.visualizations.world_map_visualizer import MapVisualizer


def main():

    st.title("Hello Coffee World!")

    folium_static(plot_map())

    show_tables()

    add_forms()
    remove_forms()


def show_tables():

    TABLE_CHOICES = [
        ("none", "none"),
        ("coffees", coffees),
        ("roasteries", roasteries),
        ("countries", countries),
    ]

    option = st.selectbox(
        "Show Table",
        options=TABLE_CHOICES,
        format_func=lambda x: x[0],
    )

    if option[1] == "none":
        pass
    else:
        st.dataframe(pd.DataFrame([dict(x) for x in option[1]]))


def add_forms():

    with st.expander("Add Entry"):
        col1, col2, col3 = st.columns(3)

        with col1:
            add_coffee_form()
        with col2:
            add_roastery_form()
        with col3:
            add_country_form()


def remove_forms():

    with st.expander("Delete Entry"):
        col1, col2, col3 = st.columns(3)

        with col1:
            remove_coffee_form()
        with col2:
            remove_roastery_form()
        with col3:
            remove_country_form()

def add_coffee_form():
    st.header("Coffee")
    with st.form(key="add_coffee", clear_on_submit=True):
        name = st.text_input("Name")
        country_of_origin = st.selectbox(
            "Country of Origin", (country.name for country in countries)
        )
        roastery = st.selectbox(
            "Roastery", (roastery.name for roastery in roasteries)
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
    st.header("Coffee")
    with st.form(key="remove_coffee", clear_on_submit=True):
        coffee_id = st.text_input("ID")
        submit = st.form_submit_button("Remove")
        if submit:
            db.remove_row(
                "coffee", (int(coffee_id),)
            )
            st.experimental_rerun()


def add_roastery_form():
    st.header("Roastery")
    with st.form(key="add_roastery", clear_on_submit=True):
        name = st.text_input("Name")
        country = st.selectbox(
            "Country", (country.name for country in countries)
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
    st.header("Roastery")
    with st.form(key="remove_roastery", clear_on_submit=True):
        roastery_id = st.text_input("ID")
        submit = st.form_submit_button("Remove")
        if submit:
            db.remove_row(
                "roastery", (int(roastery_id),)
            )
            st.experimental_rerun()


def add_country_form():
    st.header("Country")
    with st.form(key="add_country", clear_on_submit=True):
        name = st.text_input("Name")
        submit = st.form_submit_button("Add")
        if submit:
            db.insert_row("country", (name,))
            st.experimental_rerun()


def remove_country_form():
    st.header("Country")
    with st.form(key="remove_country", clear_on_submit=True):
        country_id = st.text_input("ID")
        submit = st.form_submit_button("Remove")
        if submit:
            db.remove_row("country", (int(country_id),))
            st.experimental_rerun()


def plot_map():

    visualizer = MapVisualizer()
    return visualizer.plot_coffees_by_country(coffees)


if __name__ == "__main__":

    db = CoffeeDB()
    data_loader = PostgresDataLoader(db=db)

    countries, roasteries, coffees = data_loader.get_data()

    main()
