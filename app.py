import streamlit as st
import pandas as pd
import os
from io import BytesIO

# start your app

st.set_page_config(page_title="Data-sweeper", layout="wide")

# custom css
st.markdown(
 """
 <​style>
 .stApp{
 background-color: black;
 color:white;
 }
 <​/style>
 """,
 unsafe_allow_html=True
)

st.title("💿 Data-sweeper sterling integerator by Soniya")
st.write("transform your file between csv & Excel format with build in data cleaning & visualization ")

hashtag#file uploader
uploaded_files = st.file_uploader("Upload your files (accepts csv or Excel):", type=["cvs", "xlsx"], accept_multiple_files=(True)) 

import os
import pandas as pd
import streamlit as st

if uploaded_files:
 for file in uploaded_files:
 file_ext = os.path.splitext(file.name)[-1].lower()

 if file_ext == ".csv":
 df = pd.read_csv(file)
 elif file_ext == ".xlsx": 
 df = pd.read_excel(file)
 else:
 st.error(f"Unsupported file type: {file_ext}")
 continue 


 # file detail
 st.write("🔎 preview the head of tha dataframe")
 st.dataframe(df.head())

 # data cleaning options
 st.subheader("🛠️ data cleaning options")
 if st.checkbox(f"clean data for {file.name}"):
 col1, col2 = st.columns(2)
 with col1:
 if st.button(f" remove duplicate from the file : {file.name}"):
 df.drop_duplicates(inplace=True)
 st.write("duplicae removed!")

 with col2:
 if st.button(f"fill mising values for {file.name}"):
 numeric_cols = df.select_dtypes(include=["number"]).columns
 df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
 st.write("✔️ Missing value have beeen filled!")
 
 st.subheader("🎯select columns to keep")
 columns = st.multiselect(f"choose columns for{file.name}",df.columns,default=df.columns)
 df = df[columns]

 # data visualation
 st.subheader("📊data visualization")
 if st.checkbox(f"show visualization for {file.name}"):
 st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])

 # conversion option
 st.subheader("🔁conversion option")
 conversion_type = st.radio(f"convert {file.name} to :" , ["csv", "Excel"], key=file.name)
 if st.button(f"convert{file.name}"):
 buffer = BytesIO()
 if conversion_type=="csv":
 df.to.csv(buffer,index=False)
 file_name =file.name.replace(file_ext,"csv")
 mine_type = "text/csv"

 elif conversion_type == "Excel":
 df.to.to_excel(buffer,index=False)
 file_name = file.name.replace(file_ext,".xlsx")
 mime_type = "application/vnd.openxmlformats-officeducument.spreadsheetml.sheet"
 buffer.seek(0)

 st.download_button(
 label=f"Download {file.name} as {conversion_type}",
 data= buffer,
 file_name= file_name,
 mime= mime_type
 )
st.success("All files processed successfully!🎉")

Seen by soniya dawood at 12:11 AM.
