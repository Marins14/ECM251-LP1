import streamlit as st 

st.title("HOME 🤗")
st.write("Estou começando a fazer a minha lojinha, fé que sai 😎")
st.markdown(" ## Os novos jogos estão sempre em exposição!")

def baitado():
    st.image(image = "assets/confia.jpg", caption = "VOCE FOI BAITADO! 🤣")
st.button(
    label= "CLICA AEW MEU JOVI 😎",
    help="CONFIA🤑",
    on_click = baitado
)

st.sidebar.title("Pagamentos 🤑")
