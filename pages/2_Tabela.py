import streamlit as st
import pandas as pd

st.title('Tabelas com os Dados')

url='https://raw.githubusercontent.com/Renan-Carneiro/TechExpVinho/main/ExpVinhoTratado.csv'
df = pd.read_csv(url, index_col=0)

#agrupando pela soma de litros e preço
tabela = df.groupby('País').agg({'Litros Exportados': 'sum', 'Preço Dólar': 'sum'}).reset_index()

#dropando linhas onde ambos valores são 0
tabela = tabela.loc[(tabela['Preço Dólar'] != 0) | (tabela['Litros Exportados'] != 0)]

# por preço em ordem decrescente
tabela_preco = tabela.sort_values(by='Preço Dólar', ascending=False).reset_index(drop=True)
tabela_preco.index += 1

# por litros em ordem decrescente
tabela_litros = tabela.sort_values(by='Litros Exportados', ascending=False).reset_index(drop=True)
tabela_litros.index += 1

#função para mostrar em milhões com 3 casa decimais, ou outro formato se for muito pequeno
def format_magnitude(x):
    if abs(x) >= 0.1 * 1e6:
        return "{:.3f} Milhões".format(x / 1e6)
    elif abs(x) >= 1e3:
        return "{:.1f} mil".format(x / 1e3)
    else:
        return "{:.0f}".format(x)

#modificando valores na tabela de preço
tabela_preco['Preço Dólar'] = tabela_preco['Preço Dólar'].apply(format_magnitude)
tabela_preco['Litros Exportados'] = tabela_preco['Litros Exportados'].apply(format_magnitude)

#modificando valores na tabela de litros
tabela_litros['Preço Dólar'] = tabela_litros['Preço Dólar'].apply(format_magnitude)
tabela_litros['Litros Exportados'] = tabela_litros['Litros Exportados'].apply(format_magnitude)

#adicionando uma observação para o país de origem
origem = pd.DataFrame({'Observação': ['País de origem: Brasil']})
tabela_preco = pd.concat([tabela_preco.iloc[:1], origem, tabela_preco.iloc[1:]], ignore_index=True)
tabela_litros = pd.concat([tabela_litros.iloc[:1], origem, tabela_litros.iloc[1:]], ignore_index=True)
# Mostrando com st.dataframe
st.write('Tabela por Litros Exportados')
st.dataframe(tabela_litros)

st.write('Tabela por Preço')
st.dataframe(tabela_preco)

