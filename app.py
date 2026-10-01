import streamlit as st

NUBE = "https://nube3.protcell.com/index.php/s/9P8R8E8mQW4aR2k"

st.set_page_config(page_title="ARIELMONTANO", layout="centered")
st.title("ARIELMONTANO")
st.write("Tocá el botón para entrar a tu nube privada")
st.link_button("👉 ENTRAR A MI NUBE", NUBE, use_container_width=True)
st.caption("© 2026 Ariel Montano - Protcell")
