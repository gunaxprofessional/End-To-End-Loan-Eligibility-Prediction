import streamlit as st
import pandas as pd
import pickle

# Load the saved model, scaler, and encoder
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

# Create a form for users to input data
st.write('# Loan Prediction App')

gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Married', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
applicant_income = st.slider('Applicant Income', min_value=150, max_value=81000, value=5000, step=100)
coapplicant_income = st.slider('Coapplicant Income', min_value=0, max_value=41667, value=0, step=100)
loan_amount = st.slider('Loan Amount', min_value=9, max_value=700, value=100, step=1)
loan_amount_term = st.slider('Loan Amount Term', min_value=12, max_value=480, value=360, step=1)
credit_history = st.selectbox('Credit History', ['0', '1'])
property_area = st.selectbox('Property Area', ['Rural', 'Semiurban', 'Urban'])

# Encode the categorical features
data = {'Gender': [gender], 'Married': [married], 'Dependents': [dependents],
        'Education': [education], 'Self_Employed': [self_employed], 'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income], 'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_amount_term], 'Credit_History': [credit_history],
        'Property_Area': [property_area]}
df = pd.DataFrame(data)

object_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']

df[object_cols] = encoder.transform(df[object_cols])

# Scale the numerical features
df_scaled = scaler.transform(df)

st.write('## Prediction')

if st.button('Predict'):
    result =  model.predict(df_scaled)
    if result == 0:
        st.error('Sorry, your loan application has been rejected.')
    else:
        st.success('Congratulations! Your loan application has been approved.')
