import streamlit as st 
if "baitado" not in st.session_state:
    st.session_state["baitado"] = False

def baitado():
    st.session_state["baitado"] = not st.session_state["baitado"]

main, trolei = st.tabs(["HOME","AH NEGAO"])
with main:
    st.title("HOME 🤗")
    st.write("Estou começando a fazer a minha lojinha, fé que sai 😎")
    st.markdown(" ## Os novos jogos estão sempre em exposição!")
    st.write("Loja em desenvolvimento...Aguarde!")

with trolei:
    st.button(
        label= "CLICA AEW MEU JOVI 😎",
        help="TEM CERTEZA DISSO ?🤪",
        on_click = baitado
    )
    if st.session_state["baitado"]:
        st.image(image = "assets/confia.jpg", caption = "VOCE FOI BAITADO! 🤣")




st.sidebar.title("Pagamentos 🤑")
