import streamlit as st

st.title("🔐 Mensagem Secreta")

senha = st.text_input("Digite a senha mágica para revelar a mensagem:", type="password")

if senha == "amor":
    st.balloons()
    st.success("💌 Você é muito especial! Nunca se esqueça disso.")
elif senha:
    st.warning("Senha incorreta! Tente novamente.")