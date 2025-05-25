import streamlit as st

st.set_page_config(page_title="Menu Interativo", layout="wide")

st.markdown("""
    <style>
    .titulo {
        font-size:50px;
        text-align: center;
        color: #FF4B4B;
        animation: piscar 1s infinite;
    }
    @keyframes piscar {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="titulo">🎉 Jefferson! 🎉</p>', unsafe_allow_html=True)
st.info("Escolha uma das opções no menu à esquerda 👈")
