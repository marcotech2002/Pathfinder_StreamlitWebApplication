import streamlit as st


st.set_page_config(
    page_title="Gestão de clientes",
    page_icon="📓"
)
consultation_page = st.Page("pages/consultation.py", title="Consulta", icon=":material/list:")
registration_page = st.Page("pages/registration.py", title="Cadastro", icon=":material/add_circle:")

pg = st.navigation([consultation_page, registration_page])
pg.run()