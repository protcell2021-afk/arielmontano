import streamlit as st

NUBE = "https://nube3.protcell.com/index.php/s/9P8R8E8mQW4aR2k"

st.set_page_config(page_title="ARIELMONTANO", layout="centered")
st.markdown(f'<meta http-equiv="refresh" content="0; url={NUBE}">', unsafe_allow_html=True)
st.title("ARIELMONTANO")
st.write("Redirigiendo a tu nube privada...")
st.write(f"Si no te lleva solo, toca aqui: {NUBE}")
