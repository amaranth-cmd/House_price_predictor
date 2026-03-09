import streamlit as st
import joblib
import numpy as np
#loading the trained model
model = joblib.load('housing_model.pkl')
#main eading
st.title('House Prices Predictor')
st.write('Enter the house information to get prediction:')

# Numeric inputs
area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

# Binary encoded categorical inputs
mainroad = st.selectbox("Main Road", ["yes","no"])
guestroom = st.selectbox("Guest Room", ["yes","no"])
basement = st.selectbox("Basement", ["yes","no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes","no"])
airconditioning = st.selectbox("Air Conditioning", ["yes","no"])
prefarea = st.selectbox("Preferred Area", ["yes","no"])

# Ordinally encoded categorical input
furnishingstatus = st.selectbox("Furnishing Status", ["unfurnished","semi-furnished","furnished"])

# Create predict button
if st.button("Predict Price"):
    # Map inputs to numbers
    features = np.array([[area, bedroooms, bathrooms, stories,
                          1 if mainroad=="yes" else 0,
                          1 if guestroom=="yes" else 0,
                          1 if basement=="yes" else 0,
                          1 if hotwaterheating=="yes" else 0,
                          1 if airconditioning=="yes" else 0,
                          parking,
                          1 if prefarea=="yes" else 0,
                          {"unfurnished":0,"semi-furnished":1,"furnished":2}[furnishingstatus]
                         ]])

    # Make prediction
    prediction = model.predict(features)