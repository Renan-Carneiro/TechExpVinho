import streamlit as st

st.title('Relatório:')
# Embed the reveal.js presentation using an iframe
iframe_code = '<iframe src="https://onedrive.live.com/embed?resid=1F95875ED93EE176%2196167&amp;authkey=!AJgTggXUq0HIwY0&amp;em=2&amp;wdAr=1.7777777777777777" width="1360px" height="768px" frameborder="0">Este é um apresentação do <a target="_blank" href="https://office.com">Microsoft Office</a> incorporado, da plataforma <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe>'

# Render the iframe code
st.markdown(iframe_code, unsafe_allow_html=True)
