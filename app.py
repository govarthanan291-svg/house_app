import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.set_page_config(page_title="House Price Prediction", layout="centered")

# CSS
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #FFD700, #FFC300);
}
h1 {
    text-align: center;
    color: #4B0000;
    text-shadow: 2px 2px 6px green;
}
div.stButton > button {
    background-color: #8B0000;
    color: white;
    width: 100%;
    height: 3em;
    font-size: 18px;
    border-radius: 10px;
    box-shadow: 0px 0px 12px green;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏠 House Price Prediction App</h1>", unsafe_allow_html=True)

# Inputs (8 Features)
area = st.number_input("Area (sqft)")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
floors = st.number_input("Floors")
parking = st.number_input("Parking Spaces")
yearbuilt = st.number_input("Year Built")
location_score = st.number_input("Location Score (1-10)")
size = st.number_input("House Size Category")

if st.button("Predict House Price"):
    input_data = np.array([[area, bedrooms, bathrooms, floors,
                            parking, yearbuilt, location_score, size]])

    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ₹ {int(prediction[0])}")
