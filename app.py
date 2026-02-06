import xgboost
import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open("house_price_model.pkl", "rb"))

# Page Config
st.set_page_config(page_title="House Price Prediction", layout="centered")

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #FFD700, #FFC300);
}

.main {
    background-color: transparent;
}

h1 {
    text-align: center;
    color: #4B0000;
    text-shadow: 2px 2px 5px green;
}

label {
    color: black;
    font-weight: bold;
}

div.stButton > button {
    background-color: #8B0000;
    color: white;
    height: 3em;
    width: 100%;
    border-radius: 10px;
    font-size: 18px;
    box-shadow: 0px 0px 12px green;
}

div.stButton > button:hover {
    background-color: #5C0000;
    color: #FFD700;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🏠 House Price Prediction App</h1>", unsafe_allow_html=True)

# Inputs
area = st.number_input("Enter Area (sqft)", min_value=0)
bedrooms = st.number_input("Enter Number of Bedrooms", min_value=0)
bathrooms = st.number_input("Enter Number of Bathrooms", min_value=0)

# Predict Button
if st.button("Predict House Price"):
    input_data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ₹ {int(prediction[0])}")

