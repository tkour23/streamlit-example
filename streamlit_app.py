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

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
