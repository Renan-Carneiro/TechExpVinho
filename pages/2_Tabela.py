import streamlit as st
import pandas as pd

st.title('Placeholder')

url='https://raw.githubusercontent.com/Renan-Carneiro/TechExpVinho/main/ExpVinhoTratado.csv'
df = pd.read_csv(url, index_col=0)

st.write('Tabela')
st.write(df)