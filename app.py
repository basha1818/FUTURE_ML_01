import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Sales Forecasting App")

st.write("Enter details to predict sales")

# Inputs
store = st.number_input("Store ID")
temperature = st.number_input("Temperature")
fuel_price = st.number_input("Fuel Price")
cpi = st.number_input("CPI")
unemployment = st.number_input("Unemployment")
holiday = st.selectbox("Holiday (0 = No, 1 = Yes)", [0, 1])
year = st.number_input("Year")
month = st.number_input("Month")
week = st.number_input("Week")

# Prediction
if st.button("Predict"):
    input_data = np.array([[store, holiday, temperature, fuel_price, cpi, unemployment, year, month, week]])
    
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Weekly Sales: {prediction[0]}")
