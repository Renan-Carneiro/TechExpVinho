import streamlit as st

import streamlit as st

# Sample data (replace with your actual data)
student_data = [
    {"nome": "Renan Carneiro", "matricula": "RM352715"},
    {"nome": "Vanessa Andrade", "matricula": "RM352921"},
    {"nome": "Frederico Quesado", "matricula": "RM352633"},
    {"nome": "Lucas Tabelini", "matricula": "RM352725"},
    # Add more students as needed
]

# Page title
st.title("Grupo Responsável")

# Display student information using badges
for student in student_data:
    st.markdown(
        f"### {student['nome']} ![Badge](https://img.shields.io/badge/Matrícula-{student['Matricula']}-brightgreen)"
    )