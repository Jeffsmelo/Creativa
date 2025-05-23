import streamlit as st
from streamlit.components.v1 import html

st.title("🎁 Surpresa Visual")

st.markdown("Clique no botão abaixo para uma surpresa animada:")

if st.button("Mostrar Surpresa"):
    html("""
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
      <iframe src="https://giphy.com/embed/3o7aD4Wb2g2UB5A0gY" 
        width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
    </div>
    """, height=400)