# Matheus Marins Bernardello RA: 20.00286-6
from models.user import User
import streamlit as st
import os
def update_user_db(user_db):
    status_user_update = True
    login_info = open(".streamlit/secrets.toml",'w')
    login_info.write("[passwords]")
    login_info.close()
    for user in user_db:
        username = user.get_Username()
        user_password = user.get_password()
        user_str = f'{username} = "{user_password}"'
        login_info = open(".streamlit/secrets.toml",'r')
        login_info_read = login_info.read()
        login_info.close()
        if f'{username} =' in login_info_read:
                st.write(f'Nome de usuário:"{username}" já está em uso!')
                status_user_update = False
        else:
            login_info = open(".streamlit/secrets.toml",'a')
            login_info.write(f'\n{user_str}')
            login_info.close()
    return status_user_update

class UserController():
    def __init__(self) -> None:
        self._users = [User()]
        update_user_db(self._users)
    
    def add_user(self, username, email, password, cpf, birthdate, name):
        Aux = User(username, email, password, cpf, birthdate, name)
        self._users.append(Aux)
        return update_user_db(self._users)
    
    def get_Users(self,user):
        return self._users[user]
    
    def get_User(self,username):
        for user in self._users:
            if (username == user.get_Username()) or (username == user.get_Email()):
                return user
    
    def get_Quantidade_User(self):
        return len(self._users)
    
    def checkUser(self, user):
        return user in self._users