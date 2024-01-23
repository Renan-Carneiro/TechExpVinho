import streamlit as st

def authenticate(password):
    # Hardcoded password for demonstration purposes
    return password == st.secrets["db_senha"]
def embed_jotform_alternative():
    html_code = """
    <div class="jotform-embed" style="min-height: 1px;" data-id="23339603950805806" data-type="interactive" data-iframesource="www.jotform.com"></div>
    <script>(function(doc, id){var scripts=doc.getElementsByTagName("script")[0]; if (!doc.getElementById(id)){var script=doc.createElement("script"); script.async=1; script.id=id; script.src="https://cdn.jotfor.ms/s/umd/latest/for-report-embed.js"; scripts.parentNode.insertBefore(script, scripts);}})(document, "jotform-async");</script>
    """
    st.components.v1.html(html_code, height=1500)

def show_sensitive_page():
    st.title("Relatório")

    # Create an empty container for the text input
    password_input = st.empty()

    # Get the user input from the session state
    password = st.session_state.get("password", "")

    # Check if the user input matches the password
    if not authenticate(password):
        # Display the text input box
        password_input.text_input("Digite aqui a senha:", value=password, type="password", key="password")
        st.error("Authentication failed. Access denied.")
    else:
        # Clear the text input box
        password_input.empty()
        embed_jotform_alternative()

# Example usage
show_sensitive_page()