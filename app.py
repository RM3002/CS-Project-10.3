import streamlit as st

from feature01 import return_even
from feature02 import return_odd 
original_list = [i for i in range(10)]

even_list = return_even(original_list)

odd_list= return_odd(original_list)

st.write("hooray we connected everything")

st.write(even_list)

st.write(odd_list)
