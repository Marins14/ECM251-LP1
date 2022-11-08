import streamlit as st
# COM O SQL ESPERO QUE O BUg DO STREAMLIT PARE
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
        for coluna in colunas:
            with coluna:
                if st.session_state["colunas_aux"] < st.session_state["produtos"].get_Quantidade_Produtos():
                    st.image(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Imagem(), st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Descricao())
                    st.write("R$ "+ str(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Valor()))
                    if st.button("Adicionar ao carrinho", key = st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Keyword()):
                        st.session_state["carrinho"].adicionar(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]))
                        st.write("Produto adicionado ao carrinho!")
            st.session_state["colunas_aux"] += 1                    
            if st.session_state["colunas_aux"] >= st.session_state["produtos"].get_Quantidade_Produtos():
                st.session_state["colunas_aux"] = st.session_state["produtos"].get_Quantidade_Produtos()