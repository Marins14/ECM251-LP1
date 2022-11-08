import streamlit as st
from controllers.cadastro_controller import *
from controllers.user_controller import UserController

# Só foi passado para uma pasta diferente, porem contina a mesma lógica de login do T3
# Retorna 'True' se o usuário/senha digitada estiver correto.
def Teste_User():
        contador = 0
        while contador < st.session_state["users_db"].get_Quantidade_User():
            aux = st.session_state["users_db"].get_Users(contador)
            st.write(aux)
            contador += 1

def Login():
    if "users_db" not in st.session_state:
        st.session_state["users_db"] = UserController()
    if "login_true" not in st.session_state:
        st.session_state["login_true"] = False
    
    def password_entered():
        # Checa se o usuário/senha digitado está correto.
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"] == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            st.session_state["login_true"] = True
            # Apaga a senha usada da session_state atual.
            del st.session_state["password"]  
            # del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False
    
    login,cadastro = st.tabs(["Página Inicial","Cadastre-se"])
    
    if (st.session_state["login_true"] != True):
        with cadastro:
            Cadastro()
            # if st.button("Teste Users",key="Teste_U"):
            #     Teste_User()
    else: 
        with cadastro:
            st.write("Usuário Logado.")
    
    with login:
        if "password_correct" not in st.session_state:
            # Inicialização, exibe o local para digitação de usuário e senha.
            st.text_input(label="Digite seu E-mail:", key="username")
            st.text_input(label="Digite sua Senha:", type="password", key="password")  
            if st.button(label="Login"):
                password_entered()
            return False
        
        elif not st.session_state["password_correct"]:
            # Senha incorreta - exibe mensagem de erro e permite digitar novamente.
            st.text_input(label="Digite seu E-mail:", key="username")
            st.text_input(label="Digite sua Senha:", type="password", key="password")  
            if st.button(label="Login"):
                password_entered()
            st.error("Usuário/senha incorreto.")
            return False
        else:
            # Se a sennha for correta.
            return True