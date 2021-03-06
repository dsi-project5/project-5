import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import streamlit.components.v1 as components
import zipfile

import pickle

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

st.title('Clare Drive by Road Prophet')

@st.cache
def load_data():
    accidents_df_1 = pd.read_csv('./data/US_Accidents_CleanedUp_Jan26-1.csv.gz')
    accidents_df_2 = pd.read_csv('./data/US_Accidents_CleanedUp_Jan26-2.csv.gz')
    #accidents_df_3 = pd.read_csv('./US_Accidents_CleanedUp_Jan26-3.csv.gz')
    #accidents_df_4 = pd.read_csv('./US_Accidents_CleanedUp_Jan26-4.csv.gz')
    #accidents_df_5 = pd.read_csv('./US_Accidents_CleanedUp_Jan26-5.csv.gz')
    return pd.concat([accidents_df_1, accidents_df_2], axis=0)

@st.cache
def load_test_csv():
    accidents_test_csv = pd.read_csv('./data/selected_test.csv')
    return accidents_test_csv

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

@st.cache(allow_output_mutation=True)
def load_model():
    file = zipfile.ZipFile('./models/randomforest_lmodel.p.zip', 'r')
    return pickle.load(file.open('randomforest_lmodel.p'))

@st.cache(allow_output_mutation=True)
def load_sample():
    return test_data.sample()

def get_dummy_col_set(df, prefix):
    county_cols = [col for col in df.columns if col.startswith(prefix)]
    for col in county_cols:
        if (df[col].values == 1):
            return col

def get_twilight(twilight):
    switcher={
        'Sunrise/Sunset':'sunrise_sunset',
        'Civil':'civil_twilight',
        'Nautical':'nautical_twilight',
        'Astronomical':'astronomical_twilight'
    }
    return switcher.get(twilight)


accidents_test_csv_df = load_test_csv()
weather_conditions = accidents_test_csv_df['weather_condition'].unique()
counties = accidents_test_csv_df['county'].unique()

temp = st.sidebar.slider('Temperature (F):', -30, 140, 1)

wind_chill = st.sidebar.slider('Wind Chill (F):', -50, 120, 1)

humidity = st.sidebar.slider('Humidity (%):', 0, 100, 1)

visibility = st.sidebar.slider('Visibility (mi):', 0, 60, 1)

precipitation = st.sidebar.slider('Precipitation (in):', 0, 10, 1)

hour = st.sidebar.slider('Hour:', 0, 23, 1)

month = st.sidebar.slider('Month:', 1, 12, 1)

weather_cond = st.sidebar.selectbox('Weather Condition', weather_conditions)

crossing = st.sidebar.checkbox('Crossing')
junction = st.sidebar.checkbox('Junction')
stop_sign = st.sidebar.checkbox('Stop Sign')
traffic_signal = st.sidebar.checkbox('Traffic Signal')
twilight = st.sidebar.select_slider('Twilight:', options=['Sunrise/Sunset', 'Civil', 'Nautical', 'Astronomical'])
county = st.sidebar.selectbox('Select the county', counties)



test_data = load_test_data()
X_test = load_sample()
X_test['temperaturef'] = temp
X_test['humidity'] = humidity
X_test['visibilitymi'] = visibility
X_test['precipitationin'] = precipitation
X_test['crossing'] = crossing
X_test['stop'] = stop_sign
X_test['junction'] = junction
X_test['traffic_signal'] = traffic_signal
X_test['wind_chillf'] = wind_chill

# first reset all twilight variables
X_test[['sunrise_sunset','civil_twilight', 'nautical_twilight', 'astronomical_twilight']] = 0

# then set the selected one
twilight_field = get_twilight(twilight)
X_test[twilight_field] = 1

# First unset current dummary variable
county_field_to_unset = get_dummy_col_set(X_test, 'county_')
X_test[county_field_to_unset] = 0

# Then set the new selected variable
county_field_name = 'county_'+county
X_test[county_field_name] = 1

# First unset current dummary variable
weather_cond_field_to_unset = get_dummy_col_set(X_test, 'weather_condition_')
X_test[weather_cond_field_to_unset] = 0

# Then set the new selected variable
weather_cond_field = 'weather_condition_'+weather_cond
X_test[weather_cond_field] = 1


# First unset current dummary variable
hour_field_to_unset = get_dummy_col_set(X_test, 'start_hour_')
X_test[hour_field_to_unset] = 0

# Then set the new selected variable
hour_field_name = 'start_hour_'+str(hour)
X_test[hour_field_name] = 1

# First unset current dummary variable
month_field_to_unset = get_dummy_col_set(X_test, 'month_')
X_test[month_field_to_unset] = 0

# Then set the new selected variable
month_field_name = 'month_'+str(month)

X_test[month_field_name] = 1


model_that_was_pickled = load_model()
X_test_sc = scale_test_data(X_test)
predicted = model_that_was_pickled.predict_proba(X_test_sc)
predicted_df = pd.DataFrame({'Severity': ['Severity 1', 'Severity 2', 'Severity 3', 'Severity 4'], 'Probability':predicted[0]})
st.subheader('Probabilities of an accident severity')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim(0, 1.0)

# Ref - https://stackoverflow.com/questions/64068659/bar-chart-in-matplotlib-using-a-colormap
my_cmap = plt.get_cmap("YlOrRd")
rescale = lambda y: (y - np.min(y)) / (np.max(y) - np.min(y))

ax.barh(predicted_df['Severity'], predicted_df['Probability'], color=my_cmap(rescale(predicted_df['Probability'])))
st.write(fig)

#st.write('X_test value', X_test.index)



#st.write(month_field_to_unset + '#')
#st.write(hour_field_name + '#')
#st.write(twilight_field + '#')
#st.write(county_field_to_unset + '#')
#st.write(month_field_name + '#')
#st.write(hour_field_to_unset + '#')
#st.write(weather_cond_field + '#')
#st.write(weather_cond_field_to_unset + '#')
#st.write(county_field_name + '#')
#f = open('./resources/kepler_ca_map.html')
#components.html(f.read(), width=800, height=800)
