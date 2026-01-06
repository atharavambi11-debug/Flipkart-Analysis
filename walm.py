import streamlit as st
import pandas as pd     
import numpy as np
import joblib

st.title("Walmart Sales Prediction")
st.header("Enter the features to predict sales")
st.write("This app predicts Walmart sales based on various features.") 
model = joblib.load("walmart_sales_model.pkl")

x1 = st.number_input("Temperature", 0.0, 100.0, 45.0)
x2 = st.number_input("Fuel Price", 1.0, 150.0, 2.5)
x3 = st.number_input("CPI", 100.0, 300.0, 210.0)
x4 = st.number_input("Unemployment", 1.0, 15.0, 8.0)
x5 = st.selectbox("Is Holiday", options=[0, 1], index=1)
x6 = st.selectbox("Store Type A", options=[0, 1])
x7 = st.selectbox("Store Type B", options=[0, 1]) 
x8=st.selectbox("Store Type C", options=[0, 1])  
x9=st.number_input("Department",1,100,15)
x10=st.number_input("Week of Year",1,52,20)
x11=st.number_input("Year",2010,2020,2012)      
x12=st.number_input("Month",1,12,6)
x13=st.number_input("Size",1,1000,15)




button=st.button("predict sales")
if button:
    prediction = model.predict([[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]])
    st.write(f"Predicted Walmart Sales: ${prediction[0]:.2f}")
 
