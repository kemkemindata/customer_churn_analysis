## Client Churn Analysis
This project is designed to predict client attrition using a simple web application built with Streamlit. 
Users can input various attributes related to customer behavior, such as location, tenure, revenue, and activity, and the model predicts whether the client will continue with the company.

## Features

-User Input Interface:
Users can input the location, tenure, revenue, churn status (Yes/No), and regularity (activity in the last 90 days) through interactive Streamlit widgets.

-Churn Prediction Model:
The model predicts whether a customer is likely to leave or stay with the company.

-Real-time Prediction:
Once the user provides the necessary information, they can get an instant prediction about the customer's churn status.

-Data Encoding & Preprocessing:
The location and churn status inputs are encoded using pre-trained encoders to make them compatible with the machine learning model.


## Requirements:

You can install the necessary libraries by running the 'requirements.txt' file

## How It Works

-User Input:
The user provides the following details:

-Region: Selected from a list of predefined locations.

-Tenure: How long the client has been with the company (in months).

-Revenue: The client's revenue generated.

-MRG (Churn Status): A Yes/No selection indicating if the user is currently considering leaving the company.

-Regularity: The number of times the user has been active in the last 90 days.

## Data Encoding:

The REGION and MRG values are encoded using pre-trained encoders (joblib_Encoder.sav) to make them model-compatible.

## Prediction:

The data is passed into a pre-trained machine learning model (joblib_clf.sav) to predict whether the customer will churn (leave) or not. The result is then displayed to the user.


## Model Details

The model used in this project is a pre-trained classification model that was saved using Joblib. The dataset used for training contains customer information and their churn behavior, which the model learns to predict.


## Folder Structure

── expresso.py                # Main Streamlit app file


── joblib_Encoder.sav         # Pre-trained Label Encoder for location data

── joblib_clf.sav             # Pre-trained machine learning model

── README.md                   # Project documentation

── requirements.txt            # Dependencies



