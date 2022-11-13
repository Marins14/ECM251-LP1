# Matheus Marins Bernardello RA: 20.00286-6
import streamlit as st
class Store_Ctrl:
    def __init__(self) -> None:
        st.subheader("Destaques")
        c1,c2,c3 = st.columns(3,gap="small")
        c4,c5,c6 = st.columns(3,gap="small")
        c7,c8,c9 = st.columns(3,gap="small")
        c10,c11,c12 = st.columns(3,gap="small")
        colunas = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
        
        if "colunas_aux" not in st.session_state:
            st.session_state["colunas_aux"] = 0

# Variavel criada para evitar possiveis bugs no streamlit 
        total_jogos = 0
        total_jogos = st.session_state["jogos"].get_Quantidade_Jogos()
        for st.session_state["colunas_aux"] in range(total_jogos):
            with colunas[st.session_state["colunas_aux"]]:
                st.image(st.session_state["jogos"].get_Jogo(st.session_state["colunas_aux"]).get_Imagem(), st.session_state["jogos"].get_Jogo(st.session_state["colunas_aux"]).get_Descricao())
                st.write("R$ "+ str(st.session_state["jogos"].get_Jogo(st.session_state["colunas_aux"]).get_Valor()))
                if st.button("Adicionar ao carrinho", key = st.session_state["jogos"].get_Jogo(st.session_state["colunas_aux"]).get_Keyword()+str(st.session_state["colunas_aux"])):
                    st.session_state["carrinho"].adicionar(st.session_state["jogos"].get_Jogo(st.session_state["colunas_aux"]))
                    st.write("Produto adicionado ao carrinho!😎")