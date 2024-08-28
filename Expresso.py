import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn 
import streamlit as st
import joblib

st.header('CLIENT CHURN ANALYSIS')

locations = ['FATICK', 'DAKAR', 'LOUGA', 'TAMBACOUNDA', 'KAOLACK', 'THIES',
       'SAINT-LOUIS', 'KOLDA', 'KAFFRINE', 'DIOURBEL', 'ZIGUINCHOR',
       'MATAM', 'SEDHIOU', 'KEDOUGOU']


REGION = st.selectbox('LOCATION', [x for x in locations])
TENURE =st.slider('TENURE', 0,24,3)
#MONTANT = st.number_input('Enter your top up amount')
REVENUE = st.number_input('REVENUE')
MRG = st.radio('Are you leaving?', ['Yes', 'No'])
REGULARITY = st.number_input('How many times have you been active in the last 90 days?')
 

# Encode the user's data according to the encoder used in the program
user_input_dictionary = {'REGION': REGION,
                         'TENURE': TENURE,
                         #'MONTANT': MONTANT,
                         'REVENUE': REVENUE,
                         'MRG' : MRG,
                         'REGULARITY' : REGULARITY}


if st.button('predict'):
    # Here we want to convert user input into a dataframe
    user_data = pd.DataFrame([user_input_dictionary])

    
    le = joblib.load('joblib_Encoder.sav')
    user_data['REGION'] = le.transform(user_data['REGION'])



    # Manager for MRG
    if user_data['MRG'][0] == 'Yes':
        user_data['MRG'][0] = 0
    else:
        user_data['MRG'][0] = 1


    # Here we load the model for prediction
    model = joblib.load('joblib_clf.sav')

    prediction = model.predict(user_data)

    if prediction == 0:
        st.write('The Client will not continue with the company')
    else:
        st.write('The Client will continue with the company')














