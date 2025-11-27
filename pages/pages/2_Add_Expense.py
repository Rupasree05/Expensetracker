import streamlit as st
import sqlite3

st.set_page_config(page_title="Add Expense")

st.title("➕ Add Expense")

# Connect to database
con = sqlite3.connect("expense.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    note TEXT
)
""")

date = st.date_input("Date")
category = st.selectbox("Category", ["Food", "Travel", "Bills", "Shopping", "Other"])
amount = st.number_input("Amount", min_value=0.0, format="%.2f")
note = st.text_input("Note (Optional)")

if st.button("Add Expense"):
    cur.execute("INSERT INTO expenses (date, category, amount, note) VALUES (?, ?, ?, ?)",
                (date, category, amount, note))
    con.commit()
    st.success("Expense added successfully!")

con.close()
