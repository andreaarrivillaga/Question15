import streamlit as st
import pandas as pd


st.title("Final Exam, Question 15")


url = 'https://drive.google.com/file/d/133D1c5gIVMSogmFb502Rmg34Uj_Q6pTg'
st.write(f"trying original\n {url}")


url='https://drive.google.com/uc?id=' + url.split('/')[-2]

st.write(f"trying new\n {url}")

df=pd.read_csv(url)

st.title("Done")
