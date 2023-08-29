import streamlit as st
import pandas as pd
import numpy as np

st.title('Largest number out of given 3 number')


first_num = st.number_input("First Number",min_value=None, max_value=None, step=1)
second_num = st.number_input("Second Number",min_value=None, max_value=None, step=1)
third_num = st.number_input("Third Number",min_value=None, max_value=None, step=1)
largest_num = 0

with st.form("largest_num"):
    if first_num > second_num:
        if first_num > third_num:
            largest_num = first_num
        else:
            largest_num = third_num
    elif second_num > first_num:
        if second_num > third_num:
            largest_num = second_num
        else:
            largest_num = third_num

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Largest Number = ", largest_num)
