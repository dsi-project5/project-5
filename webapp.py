import numpy as np
import pandas as pd
import streamlit as st

st.title('Safe-O-Meter - Your guide to safe driving')

st.header('Oveview')
st.header('EDA')
st.header('Model')
st.sidebar.selectbox('State', ['CA', 'FL', 'SC'])

@st.cache
def load_data():
    accidents_df_1 = pd.read_csv('./data/US_Accidents_CleanedUp_Jan26-1.csv.gz')
    accidents_df_2 = pd.read_csv('./data/US_Accidents_CleanedUp_Jan26-2.csv.gz')
    #accidents_df_3 = pd.read_csv('./US_Accidents_CleanedUp_Jan26-3.csv.gz')
    #accidents_df_4 = pd.read_csv('./US_Accidents_CleanedUp_Jan26-4.csv.gz')
    #accidents_df_5 = pd.read_csv('./US_Accidents_CleanedUp_Jan26-5.csv.gz')
    return pd.concat([accidents_df_1, accidents_df_2], axis=0)

accidents_df = load_data()
state_count_df = pd.DataFrame(accidents_df['state'].value_counts().head(15))

st.bar_chart(state_count_df)
