import streamlit as st

st.title('Placeholder')
# Embed the reveal.js presentation using an iframe
iframe_code = '<iframe src="https://slides.com/renanmoraes/deck/embed" width="960" height="540" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>'

# Render the iframe code
st.markdown(iframe_code, unsafe_allow_html=True)
