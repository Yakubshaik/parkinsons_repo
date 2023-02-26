import os 
import pandas as pd
import streamlit as st
import plotly.express as px
from matplotlib import image

file_path = os.path.abspath(__file__)
#print(file_path)
dir_path = os.path.dirname(file_path)
#print(dir_path)
parent_dir = os.path.join(dir_path,os.pardir)
#print(" parent dir: ",parent_dir)
data_path = os.path.join(parent_dir,"resources",'data',"Parkinsondata.csv")
#print(data_path)
image_path = os.path.join(parent_dir,"resources","data","brain_image.jpg")

df=pd.read_csv(data_path)

st.balloons()
st.snow()

st.title(":red[Parkinson Dataset Visualisation] :medical_symbol:")
st.markdown("The web page describes about the **records** of the :green[**_Parkinson's_ data**] from :blue[kaggle] website.")
st.header(":black[**About Dataset**]",anchor='https://www.kaggle.com/datasets/vikasukani/parkinsons-disease-data-set')
st.caption(":violet[This might help you understand the concept to some extent]")

st.write("""This dataset is composed of a range of biomedical voice measurements from 31 people, 23 with Parkinson's disease (PD).
 Each column in the table is a particular voice measure, and each row corresponds to one of 195 voice recordings from these individuals ("name" column). 
 The main aim of the data is to discriminate healthy people from those with PD, according to the "status" column which is set to **0 for healthy** and **1 for PD.**""")

st.text("Parkinson disease is typically observed in aged people.")
st.write(df.head())
code= '''
st.write(df.head)'''
st.write("The below code can be used to display the head of dataframe.")
st.code(code,language='python')

st.write("To download the whole dataset :")

button=st.button(label="**Download**",help="To download the dataset." )
if button:
    st.write("Go to **_kaggle_** as we don't know how to upload here.")

img = image.imread(image_path)
st.image(img)