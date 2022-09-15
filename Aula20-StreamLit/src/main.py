import streamlit as st

main, info, cadastro = st.tabs(["Home","Info","Cadastro"])

with main:
    st.title("Olá mundo StreamLit 🤪❤")
    st.write("é noix 🤔")
    st.markdown("## Subtitulo de **Seção!** 😎:")
    st.code(
        """def somar(a,b):
            return a+b
    val1 = 10
    val2 = 12 
    print(somar(val1,val2))
        """,
        language= 'python'
    )
    st.code(
        """
        python -m streamlit run arquivo.py
        """
    )
    st.metric(
        label="Total da Compra(R$):",
        value= 105.92
    )
with info:
    def fui_apertado():
        print("Olá mundo")
        
    def somar_dois(v1,v2):
        resultado = v1+v2
        st.session_state["Kratos, O Bom de guerra"]=resultado
        print(resultado) 
    numero1 = st.number_input(
        label= "Valor 1",
        min_value=0.0,
        max_value=100.0,
    )
    numero2 = st.number_input(
        label= "Valor 2",
        min_value=0,
        max_value=100,
    )

    st.button(
        label= "CLICA AEW CARAIO😎",
        help="CONFIA🤑",
        on_click = somar_dois,
        kwargs = {"v1":numero1,"v2":numero2}
    )
    if "Kratos, O Bom de guerra" in st.session_state:
        st.metric(
            label="Resultado:",
            value=st.session_state["Kratos, O Bom de guerra"]
        )
    else:
        st.write("Zero cálculo")
with cadastro:
    
    col1,col2,col3 = st.columns(3)

    with col1:
        st.image(
            "https://kanto.legiaodosherois.com.br/w728-h381-gnw-cfill-gcc/wp-content/uploads/2022/03/legiao_qyQ7T5ZBC8AH.jpg.webp",
            caption= "imagem do Kleitin"
        )
        with col2:
            st.image(
            image ="assets/kleitin.webp",
            caption="Kleitin"
            )
    with col3:
        st.image(
        image ="assets/kratos.jpg",
        caption="O Bom de guerra"
        )
st.sidebar.title("Navegação")
