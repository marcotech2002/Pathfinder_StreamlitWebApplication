import streamlit as st
import datetime


def save_data(client_name, client_birthday, client_type):
    file_path = '../clients.csv'
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            first_line = file.readline().strip()
    except FileNotFoundError:
        first_line = ""
    
    with open(file_path, "a", encoding="utf-8") as file:
        # Se o arquivo estiver vazio ou sem cabeçalho, escreve o cabeçalho
        if first_line != "Nome;Data de nascimento;Tipo":
            file.write("Nome;Data de nascimento;Tipo\n")
        
        # Escreve os dados do cliente
        if client_name:
            file.write(f"{client_name};{client_birthday.strftime('%d/%m/%Y')};{client_type}\n")          
            st.session_state["success"] = True
        else:
            st.session_state["success"] = False

st.title("Cadastro de clientes")
st.divider()

client_name = st.text_input("Digite o nome do cliente", key="client_name")
client_birthday = st.date_input("Informe a data de nascimento do cliente", format="DD/MM/YYYY", min_value=datetime.date(1910, 1, 1), max_value="today")
client_type = st.selectbox("Defina o tipo de cliente",
                           ["Pessoa jurídica", "Pessoa física"])
btn_register = st.button("Cadastrar", on_click=save_data, 
                         args=[client_name, client_birthday, client_type])

if btn_register:
    if st.session_state["success"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="❌")