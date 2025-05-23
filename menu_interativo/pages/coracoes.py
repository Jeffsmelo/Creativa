import streamlit as st
import time
import random

st.title("💖 Corações Infinitos")
st.caption("Uma chuva de amor só pra você!")

heart = "❤️"

ph = st.empty()

while True:
    ph.markdown(
        "".join(
            [f'<span style="font-size:{random.randint(20,50)}px;">{heart}</span>' for _ in range(30)]
        ),
        unsafe_allow_html=True
    )
    time.sleep(0.3)