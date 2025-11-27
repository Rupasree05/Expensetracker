import streamlit as st

st.set_page_config(page_title="Home")

st.title("🏠 Home - Expense Tracker")
st.write("Welcome to your Expense Tracker App!")

st.page_link("pages/2_Add_Expense.py", label="➕ Add Expense", icon="🧾")
st.page_link("pages/3_View_Expenses.py", label="📋 View Expenses", icon="📄")
st.page_link("pages/4_Category_Summary.py", label="📊 Category Summary", icon="📊")
st.page_link("pages/5_Budget.py", label="💰 Budget Planner", icon="💰")
