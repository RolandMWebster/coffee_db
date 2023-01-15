import os

import pandas as pd
import psycopg2
import streamlit as st


DATABASE_URL = os.environ.get("DATABASE_URL")
con = psycopg2.connect(DATABASE_URL)
cur = con.cursor()

query = "select * from test_coffee"

data = pd.read_sql(query, con)

st.title("Hello Coffee World!")
st.dataframe(data=data)
