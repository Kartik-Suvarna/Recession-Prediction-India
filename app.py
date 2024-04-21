import streamlit as st # type: ignore
import pandas as pd
import numpy as np
import openpyxl

st.set_page_config(layout="wide")
st.markdown("""
<style>
.big-font {
    font-size:100px !important;
    font-align:center; !important;
    }
.small-font{
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Recession Prediction India</p>', unsafe_allow_html=True)

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("A recession is a significant decline in economic activity that lasts for an extended period. It's usually marked by a drop in Gross Domestic Product (GDP), which is the total value of goods and services produced in a country. During a recession, there's often a decrease in consumer spending, business investment, and employment. This can lead to businesses producing less, people losing their jobs, and overall economic hardship.")

with right_column:
    st.image('Recession-removebg.png',width=700)

st.markdown('<p class="small-font">Lets analyse India GDP from the 1960 to 2024</p>', unsafe_allow_html=True)

# Add a slider to the sidebar:
add_slider = st.slider(
    'Select a range of values',
    1960, 2050, (1990, 2024),1
)

st.write(add_slider)

data_raw=pd.read_excel("dataset/gdp_unemp_raw.xlsx")

chart_data = data_raw

st.line_chart(chart_data)
# Add a selectbox to the sidebar:
add_selectbox = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)




left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

    import time


if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)