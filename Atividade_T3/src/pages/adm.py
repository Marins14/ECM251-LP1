# Matheus MArins Bernardello RA: 20.00286-6
import streamlit as st 
#import base64

# Irá resolver os probelmas do streamlit quebrar o código quando solicitado cadastrar novo produto 

class Adm:
    def __init__(self) -> None:
        new_product_name = st.text_input("De um nome ao produto:",key="new_prod_name")               
        new_product_description = st.text_input("Adicione uma descrição do produto:",key="new_prod_description")
        new_product_keyword = st.text_input("Digite a 'key' do produto:",key="new_prod_key")               
        new_product_value = st.text_input("Qual o valor do produto:",key="new_prod_value")
        new_product_image = st.file_uploader("Carrega uma imagem de Capa.",
                                             key="new_prod_img",
                                             accept_multiple_files=False)
                
        if st.button("Cadastrar Produto",key="new_prod_button"):
            st.session_state["produtos"].criar_novo_produto(new_product_name,new_product_description,new_product_keyword,
            float(new_product_value),
            new_product_image)
            st.write("Cadastro feito com sucesso!")
        