import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="View Expenses")

st.title("📋 View All Expenses")

con = sqlite3.connect("expense.db")
df = pd.read_sql("SELECT * FROM expenses", con)
con.close()

if df.empty:
    st.warning("No expenses added yet.")
else:
    st.dataframe(df)
