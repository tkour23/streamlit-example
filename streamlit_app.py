from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


pip install streamlit
import streamlit as st


df =pickle.load(open('df.pkl','rb'))

st.title("Battery life prediction") pip install sklearn

maxVoltage = st.selectbox('Max. Voltage Dischar. (V)',df['Max. Voltage Dischar. (V)'].unique())

minVoltage = st.selectbox('Min. Voltage Charg. (V)',df['Min. Voltage Charg. (V)'].unique())

time = st.selectbox('Time at 4.15V (s)',df['Time at 4.15V (s)'].unique())

timeconstantcurrent = st.selectbox('Time constant current (s)',df['Time constant current (s)'].unique())

DischargeTime = st.selectbox('Discharge Time (s)',df['Discharge Time (s)'].unique())

chargingtime = st.selectbox('Charging time (s)',df['Charging time (s)'].unique())

RUL = st.number_input('RUL')

if st.button('Predict Battery life'):
    pass
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
