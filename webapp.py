import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import zipfile

import pickle

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


st.title('Safe-O-Meter - Your guide to safe driving')
st.write('[Data Dictionary](#dict)')

@st.cache
def load_data():
    accidents_df_1 = pd.read_csv('./data/US_Accidents_CleanedUp_Jan26-1.csv.gz')
    accidents_df_2 = pd.read_csv('./data/US_Accidents_CleanedUp_Jan26-2.csv.gz')
    #accidents_df_3 = pd.read_csv('./US_Accidents_CleanedUp_Jan26-3.csv.gz')
    #accidents_df_4 = pd.read_csv('./US_Accidents_CleanedUp_Jan26-4.csv.gz')
    #accidents_df_5 = pd.read_csv('./US_Accidents_CleanedUp_Jan26-5.csv.gz')
    return pd.concat([accidents_df_1, accidents_df_2], axis=0)


@st.cache
def load_test_data():
    accidents_df_test = pd.read_csv('./data/test_data.csv',index_col = 0)
    return accidents_df_test


@st.cache
def load_scaler():
    return pickle.load(open('models/standard_scaler.p', 'rb'))

def scale_test_data(X_test):
    sc = load_scaler()
    X_test_sc = sc.transform(X_test)
    return X_test_sc

@st.cache
def load_model():
    file = zipfile.ZipFile('./models/randomforest_lmodel.p.zip', 'r')
    return pickle.load(file.open('randomforest_lmodel.p'))


#accidents_df = load_data()


temp = st.slider('Select the Temperature (F):', -30, 140, 1)
st.write('Temp ', temp, 'selected')
wind_chill = st.slider('Select the Wind Chill (F):', -50, 120, 1)
st.write('Wind Chill ', wind_chill, 'selected')
humidity = st.slider('Select the Humidity (%):', 0, 100, 1)
st.write('Humidity ', humidity, '% selected')
visibility = st.slider('Select the Visibility (mi):', 0, 60, 1)
st.write('Visibility ', visibility, 'selected')
precipitation = st.slider('Select the Precipitation (in):', 0, 10, 1)
st.write('Precipitation ', precipitation, 'selected')
hour = st.slider('Select the Hour:', 0, 23, 1)
st.write('Starting Hour ', hour, 'selected')
month = st.slider('Select the Month:', 0, 23, 1)
st.write('Starting Month ', month, 'selected')
weather_cond = st.selectbox('Weather Condition', ['Clear', 'Cloudy', 'Overcast', 'Partly Cloudy', 'Mostly Cloudy', 'Scattered Clouds', 'Light Rain', 'Haze'])
st.write('Select the Weather Condition ', weather_cond, 'selected')
crossing = st.checkbox('Crossing')
junction = st.checkbox('Junction')
stop_sign = st.checkbox('Stop Sign')
traffic_signal = st.checkbox('Traffic Signal')
twilight = st.radio('Select Twilight', ('Sunrise or Sunset', 'Civil Twilight', 'Nautical Twilight', 'Astronomical Twilight'))
county = st.selectbox('Select the county', ['Los Angeles CA', 'Alameda CA'])
st.write('County ', county, 'selected')

test_data = load_test_data()
X_test = test_data.sample()
X_test['temperaturef'] = temp
X_test['humidity'] = humidity
X_test['visibilitymi'] = visibility
X_test['precipitationin'] = precipitation
X_test['crossing'] = crossing
X_test['stop'] = stop_sign
X_test['junction'] = junction
X_test['traffic_signal'] = traffic_signal
X_test['wind_chillf'] = wind_chill



run_model = st.button('Run Model')
if (run_model):
    model_that_was_pickled = load_model()
    X_test_sc = scale_test_data(X_test)
    predicted = model_that_was_pickled.predict_proba(X_test_sc)
    st.write('Based on the inputs, here is severity predicted: ', predicted)
    st.write('X_test value', X_test.index)


#f = open('./resources/kepler_ca_map.html')
#components.html(f.read(), width=800, height=800)


# Test out jumping to different sections of the same page
st.markdown("<h1 id='dict'>Data Dictionary</h1>", unsafe_allow_html=True)
st.write('contents of Data dictionary')
st.header('Kepler Demo')
st.write('Kepler Maps')
st.header('Model Demo')
st.write('Model demo content')
