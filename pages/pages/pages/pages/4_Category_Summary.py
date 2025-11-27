import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Category Summary")

st.title("📊 Category-wise Summary")

con = sqlite3.connect("expense.db")
df = pd.read_sql("SELECT category, SUM(amount) as total FROM expenses GROUP BY category", con)
con.close()

if df.empty:
    st.warning("No data available.")
else:
    st.bar_chart(df.set_index("category"))
    st.dataframe(df)
