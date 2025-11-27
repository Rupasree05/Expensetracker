import streamlit as st
import time

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.markdown("""
    <style>
    .block-container { padding-top: 4rem; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.image("logo.png", width=150)
st.markdown("<h1 style='color:#4A90E2;'>Expense Tracker</h1>", unsafe_allow_html=True)
st.write("Loading...")

# Splash delay
time.sleep(2)

# Send to Home Page
st.switch_page("pages/1_Home.py")
