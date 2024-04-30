import streamlit as st
import pandas as pd


st.title("Final Exam, Question 15")


url = 'https://drive.google.com/file/d/133D1c5gIVMSogmFb502Rmg34Uj_Q6pTg'
st.write(f"trying original\n {url}")
st.write(f"snp is {url.split('/')[-2]}")


url='https://drive.google.com/uc?id=' +"133D1c5gIVMSogmFb502Rmg34Uj_Q6pTg"

st.write(f"trying new\n {url}")

df=pd.read_csv(url)

st.title("Done")
