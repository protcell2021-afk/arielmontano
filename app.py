import streamlit as st
st.set_page_config(page_title="ARIELMONTANO", layout="centered")
LINKS = {
    "nube": "https://nube3.protcell.com/index.php/s/9P8R8E8mQW4aR2k",
    "whatsapp": "https://wa.me/50500000000",
    "home": "https://arielmontano.streamlit.app"
}
params = st.query_params
code = params.get("c", "")
if code in LINKS:
    st.markdown(f'<meta http-equiv="refresh" content="0; url={LINKS[code]}">', unsafe_allow_html=True)
    st.write(f"Redirigiendo a {code}...")
    st.link_button("Si no te redirige, toca aqui", LINKS[code])
    st.stop()
st.title("🔗 ARIELMONTANO")
st.subheader("Official Link Hub")
st.link_button("☁️ IR A MI NUBE PRIVATE CLOUD", LINKS["nube"])
st.divider()
st.write("Tu link corto:")
st.code("arielmontano.streamlit.app/?c=nube")
