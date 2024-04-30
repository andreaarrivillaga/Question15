import streamlit as st
import pandas as pd

url = 'https://github.com/andreaarrivillaga/Question15/blob/main/athlete_events.csv.gz'
st.title("Final Exam, Question 15")

df=pd.read_csv(url)

st.title("Done")
