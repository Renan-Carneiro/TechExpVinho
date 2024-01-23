import streamlit as st

st.title('Placeholder')
# Embed the reveal.js presentation using an iframe
iframe_code = <iframe src="https://slides.com/renanmoraes/minimal/embed" width="576" height="420" title="Minimal" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

# Render the iframe code
st.markdown(iframe_code, unsafe_allow_html=True)
