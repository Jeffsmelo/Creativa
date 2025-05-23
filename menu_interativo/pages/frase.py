import streamlit as st
import random

frases = [
    "Acredite nos seus sonhos e vá atrás deles!",
    "Hoje é um ótimo dia para sorrir 😄",
    "A jornada é tão importante quanto o destino.",
    "Você é mais forte do que pensa!"
]

st.title("📜 Frase do Dia")
st.success(random.choice(frases))