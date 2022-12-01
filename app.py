import streamlit as st
import pandas as pd
import pickle
st.write("Here's my first attempt to create a project:")
st.header("Division of 2 given numbers")
st.header("User input parameter")
x = st.number_input('1st number')
y = st.number_input('2nd Number')
if y!=0:
  Out = x/y
  #st.write('Division of 2 given numbers is ', x /y)
else:
  Out = "2nd Number must be Greater than 0"
  #st.write("Zero Division Error")
st.write(Out)

