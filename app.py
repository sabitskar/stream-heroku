import streamlit as st
import pandas as pd
import pickle
st.write("Here's my first attempt to create a project:")
st.header("User input parameter")
x = st.slider('x')
y = st.slider('y')
if y!=0:
  st.write('Division of 2 given numbers is ', x /y)
else:
  st.write("ZeroDivisionError")

