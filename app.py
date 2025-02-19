import streamlit as st 
import pandas as pd 
import os 
from io import BytesIO

# Set up our app

st.set_page_config(page_title='Data sweeper',layout='wide') 
st.title('Data sweeper')
st.write("transform from your file bettween CSV & Excel formats with build in data cleaning & visualization")
