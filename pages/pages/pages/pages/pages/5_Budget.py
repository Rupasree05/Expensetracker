import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Budget")

st.title("💰 Budget Planner")

con = sqlite3.connect("expense.db")
df = pd.read_sql("SELECT SUM(amount) as total FROM expenses", con)
con.close()

total_spent = df["total"][0] if df["total"][0] is not None else 0

budget = st.number_input("Set Monthly Budget:", min_value=0)

if budget > 0:
    st.write(f"Total Spent: **₹{total_spent}**")
    remaining = budget - total_spent

    if remaining >= 0:
        st.success(f"You are within budget! Remaining: ₹{remaining}")
    else:
        st.error(f"Budget exceeded by ₹{abs(remaining)}")
