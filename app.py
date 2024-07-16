import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 
import joblib
import streamlit as st 

# load model 
model_all=joblib.load('mileage.pkl')
loaded_model=model_all['model']
loaded_features=model_all['features']

# create a function to predict 
def predict(input_data): 
    # convert input_data in to dataframe 
    input_data=pd.DataFrame(input_data)
    input_data=pd.get_dummies(input_data)

    for cols in loaded_features: 
        if cols not in input_data.columns: 
            input_data[cols]=0

    new_data=new_data[loaded_features.columns]
    new_pred=loaded_model.predict(new_data)

    return new_pred

# taking user input 
st.header("Input Data for Prediction")
input_data={}
input_data['Year']=st.number_input('Year of Car Make')
input_data['run']=st.number_input('kilometers run')
input_data['fuel']=st.text_input('fuel type')
input_data['trans']=st.text_input('transmission type')
input_data['power']=st.number_input('power')
input_data['engine']=st.number_input('engine')

# createa a prediction button 
if st.button('Predict'):
    prediction=predict(input_data)
    st.write(f'Prediction"{prediction[0]}')


        


    