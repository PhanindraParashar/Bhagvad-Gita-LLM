import json 
import pandas as pd 
import numpy as np
import os
import streamlit as st

with open('gita_data_all.json', 'r') as file:
    data = json.load(file)
    
    
# create a streamlit app to display Bhagvat Gita



st.title('Bhagvat Gita')
st.subheader('Intrepretations with LLM: Zephyr-7b-Beta')

# Choose a chapter from the dropdown
chapters = list(data.keys())
chapter = st.selectbox('Select a chapter', chapters)

verses = list(data[chapter].keys())
verse = st.selectbox('Select a verse', verses)

sanskrit = data[chapter][verse]['sanskrit']
english = data[chapter][verse]['english']
interpretations = data[chapter][verse]['interpretation']
corporate = interpretations['corporate']
startup = interpretations['startup']
personal = interpretations['personal']
student = interpretations['student']

st.subheader('Sanskrit')
st.write(sanskrit)

#add a video here
st.write('Sample AI Genberated Video - Chapter 1 Verse 3')
st.video('ch1_v1.mp4')

st.write('Sample AI Genberated Audio - Chapter 1 Verse 1')
st.audio('ch1_v1.mp3')

st.subheader('English')
st.write(english)

st.subheader('Interpretations')
st.subheader('Corporate')
st.write(corporate)
st.subheader('Startup')
st.write(startup)
st.subheader('Personal')
st.write(personal)
st.subheader('Student')
st.write(student)

st.subheader('Credits')
st.write('https://www.holy-bhagavad-gita.org/')
st.write('https://huggingface.co/HuggingFaceH4/zephyr-7b-beta')
st.write('Streamlit')
st.write('OLLAMA')
