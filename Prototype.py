# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 00:45:16 2022

@author: ztbl
"""

from pycaret.classification import load_model, predict_model
import streamlit as st
import sklearn; sklearn.show_versions()
import pandas as pd
import numpy as np
import pickle
from sklearn.impute import SimpleImputer


model = load_model('Model')

 # Title Giving

def run():
    
    st.title('Online Payments Fraud Detection system')
 
 #input data
 
    Type = st.selectbox ('Type',('CASH_IN','CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'))
    
    st.write('You have selected:',Type, 'of type',type(Type))  
 
    amount = st.number_input('amount')    
    oldbalanceOrg = st.number_input('oldbalanceOrg')   
    newbalanceOrig = st.number_input('newbalanceOrig') 
 
    output = ""
    output_1 = ""
 
    
 
 #input dictrionary
    input_dict = {'Type':Type,'amount':amount,'oldbalanceOrg':oldbalanceOrg,'newbalanceOrig':newbalanceOrig}
    input_df = pd.DataFrame(input_dict ,index = [0])
  # Creating a button for analysis

    if st.button('Run Analysis'):
 # Prediction
         output = predict_model(model,data = input_df)
     
         output = str(output['Label'][0])
         if(output=='0.0'):

             output_1='Is not Fraud'

         else: 
             output_1='Is Fraud'
   

         st.success(output_1)  
 
  
 
  
 
if __name__== '__main__':
     run()            