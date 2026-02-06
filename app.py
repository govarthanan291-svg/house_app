import xgboost
import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("house_price_model.pkl")

# Page config
st.set_page_config(page_title="House Price Predictor", layout="centered")

# 🌟 GOLD THEME CSS
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #FFD700, #FFC300);
}

.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #4B0000;
    text-shadow: 2px 2px 6px green;
}

.subtext {
    text-align: center;
    color: #5C0000;
    margin-bottom: 30px;
    font-size: 18px;
}

.prediction-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #FFF3B0;
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    color: #8B0000;
    box-shadow: 0px 0px 12px green;
}

div.stButton > button {
    background-color: #8B0000;
    color: white;
    font-size: 18px;
    width: 100%;
    border-radius: 10px;
    height: 3em;
    box-shadow: 0px 0px 12px green;
}

div.stButton > button:hover {
    background-color: #5C0000;
    color: #FFD700;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🏠 House Price Predictor</div>', unsafe_allow_
