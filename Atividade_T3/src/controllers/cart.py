# Matheus Marins Bernardello RA: 20.00286-6
import streamlit as st
from datetime import datetime
class Cart_Ctrl:
    def __init__(self) -> None:
        col1,col2,col3 = st.columns([1.5,5,2.5],gap = "small")
        with col1:
            st.write("Remover:")
            for produto in range (st.session_state["carrinho"].get_Quantidade_Produtos()):
                aux = st.session_state["carrinho"].exibir_Produtos(produto)
                if st.button("Remover",key = ("Remover_"+aux.get_Keyword()+str(produto))):
                    st.session_state["carrinho"].remover(aux)
                      
        
        with col2:
            st.write("Produtos:")
            
            for jogo in range(st.session_state["carrinho"].get_Quantidade_Produtos()):
                st.write(str(st.session_state["carrinho"].exibir_Produtos(jogo)))
                st.text(" ")
               
        
        with col3:
            st.write("Resumo da Compra:")
            st.write("Quant. de Produtos: "+str(st.session_state["carrinho"].get_Quantidade_Produtos()))
            st.write("Valor total: R$ "+str(st.session_state["carrinho"].get_Valor_Total()))
            if st.button("Pagamento",key = ("pagamento")):
                st.session_state["pedido"].inserir_pedido(st.session_state["userlogged"],st.session_state["carrinho"],datetime.today().strftime('%d/%m/%Y'))
                st.write("Calma meu jovem, já estamos trabalhando para você!")
            else:
                st.write("Infelizmente não foi possivel realizar seu pedido 😢")