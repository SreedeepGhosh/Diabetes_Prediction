# app.py
import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("diabetes_model_tuned.pkl")

st.title("🩺 Diabetes Prediction App")
st.write("Enter the patient data below to predict whether they are diabetic:")

# Input fields with typical ranges from the Pima Indians Diabetes Dataset
Pregnancies = st.number_input("Pregnancies (Typical range: 0 - 17)", min_value=0, max_value=20, value=0,
                              help="Typical range: 0 - 17")
Glucose = st.number_input("Glucose (Typical range: 50 - 200 (mg/dL))", min_value=0, max_value=200, value=100,
                          help="Typical range: 50 - 200 (mg/dL)")
BloodPressure = st.number_input("Blood Pressure (Typical range: 40 - 122 (mm Hg))", min_value=0, max_value=140, value=70,
                                 help="Typical range: 40 - 122 (mm Hg)")
SkinThickness = st.number_input("Skin Thickness (Typical range: 10 - 99 (mm))", min_value=0, max_value=100, value=20,
                                 help="Typical range: 10 - 99 (mm)")
Insulin = st.number_input("Insulin (Typical range: 15 - 846 (mu U/mL))", min_value=0, max_value=900, value=80,
                          help="Typical range: 15 - 846 (mu U/mL)")
BMI = st.number_input("BMI (Typical range: 18.0 - 67.1)", min_value=0.0, max_value=70.0, value=25.0,
                      help="Typical range: 18.0 - 67.1")
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function (Typical range: 0.08 - 2.42)", min_value=0.0, max_value=3.0, value=0.5,
                      help="Typical range: 0.08 - 2.42")
Age = st.number_input("Age", min_value=1, max_value=120, value=30,
                      help="Typical range: 21 - 81 years")

# Prediction button
import pandas as pd

if st.button("Predict"):
    input_data = pd.DataFrame([[
        Pregnancies, Glucose, BloodPressure, SkinThickness, 
        Insulin, BMI, DiabetesPedigreeFunction, Age
    ]], columns=[
        'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
    ])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🔴 The patient is likely diabetic.")
    else:
        st.success("🟢 The patient is not likely diabetic.")

