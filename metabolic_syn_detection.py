#import necessary libraries
import pandas as pd
import joblib
import streamlit as st

#load model and encoder
model = joblib.load("metabolic_syn_model.pkl")
encoder = joblib.load("metabolic_syn_encoder.pkl")

#creating streamlit interface
name = "Sadiq Inuwa"
goal = "1.To predicts a particular class of anemia from the provided clinical values. 2.To confirm the legitimates of a test result !"
st.sidebar.title("ABOUT US!")
st.sidebar.caption(f"Developer: {name}.")
st.sidebar.title("CONTACTS US...")
st.sidebar.link_button("facebook", 'https://www.facebook.com/sadeeq.alhinuwa')
st.sidebar.link_button("email", 'sadiqinuwa6@gmail.com')
st.sidebar.link_button("WhatsApp", 'https://wa.me/2347067717477')
st.title("ANEMIA CLASS PREDICTION")
st.caption(f"GOAL: {goal}")


#accepting users input
Age = st.number_input("Enter patient's Age Value!")
Sex = st.selectbox("Select patient's sex!", [ "Male", "Female" ])
Marital = st.selectbox("Select patient's marital status!", ["Married","Single","Widowed","Separated"])
Race = st.selectbox("Select patient's race!", ["White","Black","Asian","Hispanic","MexAmerican"])
BMI = st.number_input("Enter patient's BMI(Body Mass Index) Value!")
UrAlbCr = st.number_input("Enter patient's UrAlbCr value!")
UricAcid = st.number_input("Enter patient's UricAcid value!")
BloodGlucose = st.number_input("Enter patient's BloodGlucose value!")
HDL =st.number_input("Enter patient's HDL value!")
Triglycerides = st.number_input("Enter patient's Triglycerides value!")


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
    predicted_data = encoder.transform(prediction_data)
    prediction = model.predict(predicted_data)
    if prediction == 1:
        st.success("Yes!")
    elif prediction == 0:
        st.warning("No!")
    else:
        st.warning("Please enter the correct inputs!")