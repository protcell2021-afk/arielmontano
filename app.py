import streamlit as st

LINKS = {
    "nube": "https://universidad-offline-3qhasdw6lvwsrtqsy3xkoc.streamlit.app/",
}

st.set_page_config(page_title="ArielMontano Link", page_icon="🔗")
query = st.query_params.get("c", "")

if query in LINKS:
    st.markdown(f'<meta http-equiv="refresh" content="0; url={LINKS[query]}">', unsafe_allow_html=True)
    st.success(f"Redirigiendo a tu nube...")
    st.link_button("IR AHORA ☁️", LINKS[query])
else:
    st.title("🔗 ARIELMONTANO")
    st.subheader("Official Link Hub")
    st.link_button("☁️ IR A MI NUBE PRIVATE CLOUD", "https://universidad-offline-3qhasdw6lvwsrtqsy3xkoc.streamlit.app/")
    st.divider()
    st.write("Tu link corto:")
    st.code("arielmontano.streamlit.app/?c=nube", language="text")
