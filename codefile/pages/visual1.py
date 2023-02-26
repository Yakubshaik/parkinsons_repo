
import os 
import pandas as pd
import streamlit as st
import plotly.express as px

file_path = os.path.abspath(__file__)
#print(file_path)
dir_path = os.path.dirname(file_path)
#print(dir_path)
parent_dir1 = os.path.join(dir_path,os.pardir)
#print(" parent dir: ",parent_dir)
parent_dir = os.path.join(parent_dir1,os.pardir)
data_path = os.path.join(parent_dir,"resources",'data',"Parkinsondata.csv")
#print(data_path)




df=pd.read_csv(data_path)

df_status = df['status'].unique()

st.header("Now, let's see some graphical representation!:balloon:")

st.write("please select the value from the select box given below to know the aspect of **PPE OVER STATUS.**")

select_box = st.selectbox(":violet[Select the status:]",df_status)

st.write("Below is the graphs of **STATUS vs PPE**")


fig_1 = px.histogram(df[df['status'] == select_box], x="PPE")
st.plotly_chart(fig_1, use_container_width=True)

