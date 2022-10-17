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


with st.title("Battery life prediction"):
    total_points = st.slider("Max. Voltage Dischar. (V)", 1.000,3.043 , 4.363)
    total_points = st.slider("Min. Voltage Dischar. (V)", 1.000, 3.022, 4.376)
    total_points = st.slider("Discharge Time (s)", 1.00, 8.69, 949261.22)
    total_points = st.slider("Time constant current (s)", 1.00, 5.98, 880728.10)
    
    num_turns = st.slider(("RUL", 0, 500, 1133)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

     markers =df.value.ge(thresh)

    # copy dates of the above row
    df['last_day'] = np.nan
    df.loc[markers, 'last_day'] = df.timestamp

    # back fill those dates 
    df['last_day'] = df['last_day'].bfill().astype('datetime64[ns]')

    df['RUL'] = (df.last_day - df.timestamp).dt.days

    # drop the columns if necessary,
    # remove this line to better see how the code works
    df.drop('last_day', axis=1, inplace=True)


calc_rul(df, 300)
