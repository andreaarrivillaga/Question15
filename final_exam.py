import streamlit as st
import pandas as pd


st.title("Final Exam, Question 15")


url = 'https://drive.google.com/file/d/133D1c5gIVMSogmFb502Rmg34Uj_Q6pTg'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]

st.title(f"trying {url}")

df=pd.read_csv(url)

st.title("Done")
