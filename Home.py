import streamlit as st
import requests

from streamlit_lottie import st_lottie



st.set_page_config(page_title='Tech Challenge: Exportação Vinhos' , page_icon='✔' , layout='wide')
st.sidebar.success("Selecione uma página acima.")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#asset
lottie_animation = load_lottieurl('https://lottie.host/111a3f73-01e4-4490-bf68-f65603ae33b8/iFJ2cro5CJ.json')

#Header
with st.container():

    st.title('Bem vindo(a)')
    st.title('Tech Challenge: Exportação Vinhos')
    st.subheader('Use a barra de navegação ao lado para navegar')
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('O Desafio')
        st.write(
            """
           No trabalho atuamos como Experts em Data Analytics em uma empresa que exporta vinhos do Brasil para o mundo.
           Nossa área é responsável pelos relatórios iniciais a serem apresentados em uma reunião de investidores e acionistas, explicando a quantidade de vinhos exportados e os fatores externos que podem vir a surgir e interferir nas análises.
            """
        )
        st.write('[FIAP](https://postech.fiap.com.br/)')
    with right_column:
        st_lottie(lottie_animation,height=300,key='vinhos')