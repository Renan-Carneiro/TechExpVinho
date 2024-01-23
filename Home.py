import streamlit as st
import requests

from streamlit_lottie import st_lottie



st.set_page_config(page_title='Controle de Procedimentos RIVOA' , page_icon='✔' , layout='wide')
st.sidebar.success("Selecione uma página acima.")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#asset
lottie_animation = load_lottieurl('https://lottie.host/71b5d1e5-c0cc-413a-9332-76e9149aa814/UxkWDNiGoE.json')

#Header
with st.container():

    st.title('Bem vindo(a)')
    st.title('Controle de Procedimentos RIVOA')
    st.subheader('Use a barra de navegação ao lado para navegar')
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Rivoa')
        st.write(
            """
            A equipe RIVOA atua no segmento da radiologia intervencionista. A especialidade utiliza métodos de imagem como ultrassonografia, RX e tomografia computadorizada para guiar os procedimentos minimamente invasivos.
            """
        )
        st.write('[Website](https://rivoa.com.br/)')
    with right_column:
        st_lottie(lottie_animation,height=300,key='medicos')