import os

import pandas as pd
import streamlit as st

from coffee_db import CoffeeDB


db = CoffeeDB()

st.title("Hello Coffee World!")
st.dataframe(data=db.get_data())

st.header("Add Coffee")
form = st.form(key="add_coffee")
with form:
    coffee_id = st.text_input("id")
    roastery = st.text_input("Roastery")
    country = st.text_input("Country")
    submit = st.form_submit_button("Add")
    if submit:
        db.insert_coffee((int(coffee_id), roastery, country,))
