import os

import pandas as pd
import psycopg2
import streamlit as st

from coffee_db import CoffeeDB


db = CoffeeDB()

st.title("Hello Coffee World!")
st.dataframe(data=db.get_data())
