import streamlit as st

NUBE = "https://nube3.protcell.com/index.php/s/9P8R8E8mQW4aR2k"

st.set_page_config(page_title="Redirigiendo...", layout="centered")

# REDIRECCION AUTOMATICA EN 1 SEGUNDO
st.markdown(f'<meta http-equiv="refresh" content="0; url={NUBE}">', unsafe_allow_html=True)

st.title("🔗 ARIELMONTANO")
st.write("Redirigiendo a tu nube privada...")
st.write("")
st.link_button("☁️ Si no te lleva, TOCA AQUI", NUBE, use_container_width=True)

st.divider()
st.caption("© 2026 Ariel Montaño - Protcell")

# Para que funcione el click tambien
st.markdown(f'<script>window.location.href = "{NUBE}";</script>', unsafe_allow_html=True)
