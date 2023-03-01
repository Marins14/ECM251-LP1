# Matheus Marins Bernardello RA: 20.00286-6
import streamlit as st
from controllers.pedido_controller import Pedido_Control
from controllers.product_controller import Product_Controller
from controllers.cart_controller import Carrinho
from controllers.loja_controller import Store_Ctrl
from controllers.cart import Cart_Ctrl
from controllers.profile_controller import Profile_Ctrl
from controllers.adm_controller import Admin_Ctrl

class Home:
    def __init__(self):
        if "carrinho" not in st.session_state:
            st.session_state["carrinho"] = Carrinho()
        st.session_state["jogos"] = Product_Controller()
        st.session_state["pedido"] = Pedido_Control()
        
        store,cart,profile,administration = st.tabs(["Loja","Carrinho","Perfil","Novos Produtos"])    
        with store:
            Store_Ctrl()
        with cart:
            Cart_Ctrl()
        with profile:
            Profile_Ctrl()
        with administration:
            Admin_Ctrl() 
        hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)