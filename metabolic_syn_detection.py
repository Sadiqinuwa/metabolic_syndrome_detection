#import necessary libraries
import pandas as pd
import joblib
import streamlit as st
import time

#load model and encoder
model = joblib.load("metabolic_syn_model.pkl")
encoder = joblib.load("metabolic_syn_encoder.pkl")

#creating streamlit interface
name = "Sadiq Inuwa"
goal = "To detects metabolic syndrome status (Yes or No) "
st.sidebar.title("Developer")
st.sidebar.caption(name)
st.sidebar.title("CONTACTS")
st.sidebar.link_button("facebook", 'https://www.facebook.com/sadeeq.alhinuwa')
st.sidebar.link_button("email", 'sadiqinuwa6@gmail.com')
st.sidebar.link_button("WhatsApp", 'https://wa.me/2347067717477')
st.title("METABOLIC SYNDROME DETECTION")
st.caption(f"GOAL: {goal}")


#accepting users input
Age = st.number_input("Enter patient's Age Value:")
Sex = st.selectbox("Select patient's gender:", [ "Male", "Female" ])
Marital = st.selectbox("Select patient's marital status:", ["Married","Single","Widowed","Separated"])
Race = st.selectbox("Select patient's race:", ["White","Black","Asian","Hispanic","MexAmerican"])
BMI = st.number_input("Enter patient's BMI(Body Mass Index) Value:")
UrAlbCr = st.number_input("Enter patient's UrAlbCr level:")
UricAcid = st.number_input("Enter patient's UricAcid level:")
BloodGlucose = st.number_input("Enter patient's Blood Glucose level:")
HDL =st.number_input("Enter patient's HDL level:")
Triglycerides = st.number_input("Enter patient's Triglycerides level:")


#prediction dataframe
if st.button("Detect Metabolic Syndrome"):
    prediction_data = pd.DataFrame({
       "Age":[Age],
       "Sex":['Sex'],
       "Marital":['Marital'],
       "Race":['Race'],
       "BMI":[BMI],
       "UrAlbCr":[UrAlbCr],
       "UricAcid":[UricAcid],
       "BloodGlucose":[BloodGlucose],
       "HDL":[HDL],
       "Triglycerides":[Triglycerides]
   })

    #transform the predicted dataframe
    progress = st.progress(0, text="Detecting Metabolic Syndrome...")
    predicted_data = encoder.transform(prediction_data)
    prediction = model.predict(predicted_data)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1, "Detecting Metabolic Syndrome...")
    progress.empty()
    if prediction[0] == 1:
        st.badge("YES! - Metabolic Syndrome Detected", color="red")
    elif prediction[0] == 0:
        st.badge("NO! - Metabolic Syndrome Not Detected", color="green")

