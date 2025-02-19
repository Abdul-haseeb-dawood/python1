import streamlit as st 
import pandas as pd 
import os 
from io import BytesIO

# Set up our app

st.set_page_config(page_title='Data sweeper',layout='wide') 


# custum css
st.markdown(
    """
    <style>
        .stApp{
        background-color: black;
        color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
)

st.title(" Data-sweeper sterling integrator by A.Haseeb")
st.write("transform from your file bettween CSV & Excel formats with build in data cleaning & visualization")

#file uploder

uploded_files = st.file_uploader("Uplode your files (accepts csv or excel ):" ,type=["csv","xlsx"],
accept_multiple_files=(True))
