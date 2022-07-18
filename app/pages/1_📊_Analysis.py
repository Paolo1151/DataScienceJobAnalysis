import streamlit as st

from config import settings

def create_sidebar():
    with st.sidebar:
        st.title("An Analysis of Data Science Jobs and Data Scientist Migration Patterns")
        st.subheader("by Paolo Dano")
        st.markdown("----")
        page = st.selectbox("Pages", options=settings.RENDERER.get_page_list())
        st.markdown("----")

    return page


st.set_page_config(
    page_title="Analysis",
    page_icon="📊",
    layout='centered',
    initial_sidebar_state='auto'
)

page = create_sidebar()
settings.RENDERER.render(page)