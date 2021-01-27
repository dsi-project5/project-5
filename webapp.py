import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from google.cloud import bigquery
import streamlit as st

st.title('Safe-O-Meter - Your guide to safe driving')

@st.cache()
def get_credentials():
    with open('dsi-team-project-75bf7059c640.json','r') as json_file:
        creds = json.load(json_file)
    return creds


@st.cache()
def get_count_by_hour():
    creds = get_credentials()
    query = """
    SELECT start_hour, count(*) FROM `dsi-team-project.accidents.accidents` group by start_hour
    """
    accidents = pd.read_gbq(query, project_id=creds['project_id'], reauth = True)
    return accidents

st.write('Accidents by Hour of Accident')
st.bar_chart(get_count_by_hour())
