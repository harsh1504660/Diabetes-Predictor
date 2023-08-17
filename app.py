import streamlit as st
import pickle
import pandas as pd
import numpy as np


df = pickle.load(open('df.pkl','rb'))
lor = pickle.load(open('lor.pkl','rb'))

st.title('Diabetes Predictor')


#age and gener 
col1 , col2 = st.columns(2)
with col1 :
    gender = st.selectbox('Gender',['Male','Female','Other'])
with col2 :
    age = st.number_input('Age')

# hypertension and heart disease
col3 , col4 = st.columns(2)
with col3 :
    hypertenstion = st.selectbox('Do you have Hypertension',['NO','YES'])
with col4 :
    heart_disease = st.selectbox('Do you have any Heart Disease',['NO','YES'])

# smoking history and bmi
col5 , col6 = st.columns(2)
with col5:
    smoking_history = st.selectbox('Smoking History',df['smoking_history'].unique())
with col6 :
    bmi = st.number_input('BMI')


#Hemoglobin
HbA1c_level = st.number_input('Himoglobin A1c in last 2-3 Months')

#blood-glucose
blood_glucose_level = st.number_input('Blood-Glucose Level In Last 2-3 Months')

if st.button('Generate Qick Result'):
    if hypertenstion=='YES':
        hypertenstion=1
    else : hypertenstion=0

    if heart_disease=='YES':
        heart_disease=1
    else :
        heart_disease =0


    query = pd.DataFrame({'gender':[gender],'age':[age],
                  'hypertension':[hypertenstion],'heart_disease':[heart_disease],'smoking_history':[smoking_history],
                  'bmi':[bmi],'HbA1c_level':[HbA1c_level],'blood_glucose_level':[blood_glucose_level]})

    result = lor.predict(query)[0]
    if result == 0:
        st.header('Congrats You Dont Have Diabetes!')
    else :
        n = lor.predict_proba(query)[0][0]
        y = lor.predict_proba(query)[0][1]
        st.header('Diabetes Positive :'+'%.2f' % y +' %')
        st.header('Diabetes Negative :'+'%.2f' % n +' %')
        st.header('We Have Detected The Diabetes, Please Take Appropiate Treatment.')
