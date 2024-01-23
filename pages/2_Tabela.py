import streamlit as st
import pandas as pd

st.title('Placeholder')

url='https://raw.githubusercontent.com/Renan-Carneiro/TechExpVinho/main/ExpVinhoTratado.csv'
df = pd.read_csv(url, index_col=0)

#agrupando pela soma de litros e preço
tabela = df.groupby('País').agg({'Litros Exportados': 'sum', 'Preço Dólar': 'sum'}).reset_index()

#dropando linhas onde ambos valores são 0
tabela = tabela.loc[(tabela['Preço Dólar'] != 0) | (tabela['Litros Exportados'] != 0)]

# por preço em ordem decrescente
tabela_preco = tabela.sort_values(by='Preço Dólar', ascending=False).reset_index(drop=True)

# por litros em ordem decrescente
tabela_litros = tabela.sort_values(by='Litros Exportados', ascending=False).reset_index(drop=True)

st.write('Tabela por Preço')
st.write(tabela_preco)
st.write('Tabela por Litros Exportados')
st.write(tabela_litros)