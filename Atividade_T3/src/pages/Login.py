import streamlit as st 
from controllers import user_controller

st.title("Vamos para parte burocrática, faça seu login: ")
st.markdown("Login")

def login():
    user = input("Digite o nome de usuario: ")
    password = input("Digite sua senha: ")
    if checkLogin == False:
        print("Nome de usuario ou senha estao errados")
    
    