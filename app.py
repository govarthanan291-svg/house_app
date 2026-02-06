import xgboost
import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("house_price_model.pkl")   # change name if your model file is different

# Page config
st.set_page_config(page_title="House Price Predictor", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
    }
    .subtext {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #e8f6f3;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #117864;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">House Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Enter the house details below</div>', unsafe_allow_html=True)

# Input form
with st.form("prediction_form"):

    GrLivArea = st.number_input("Ground Living Area", min_value=100, max_value=5000, value=1500)
    BedroomAbvGr = st.number_input("Bedrooms Above Ground", min_value=1, max_value=10, value=3)
    FullBath = st.number_input("Full Bathrooms", min_value=1, max_value=5, value=2)
    TotalBsmtSF = st.number_input("Base Area", min_value=0, max_value=3000, value=800)
    GarageCars = st.number_input("Garage Capacity", min_value=0, max_value=5, value=2)
    YearBuilt = st.number_input("Built Year", min_value=1800, max_value=2025, value=2000)
    hallArea = st.number_input("hall Area", min_value=1000, max_value=50000, value=8000)
    OverallQuality = st.number_input("Quality of house", min_value=1, max_value=10, value=7)

    submit = st.form_submit_button("Predict Price")

# Prediction
if submit:
    input_data = np.array([[GrLivArea, BedroomAbvGr, FullBath,
                            TotalBsmtSF, GarageCars, YearBuilt,
                            LotArea, OverallQual]])

    prediction = model.predict(input_data)[0]

    st.markdown(
        f'<div class="prediction-box">Predicted Price: ${prediction:,.2f}</div>',
        unsafe_allow_html=True
    )
