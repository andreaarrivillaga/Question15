import streamlit as st
import pandas as pd

DATA_URL = ('athlete_events.csv.gz')
st.title("Final Exam, Question 15")

df=pd.read_csv(DATA_URL)

st.title("Done")
