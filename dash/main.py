import streamlit as st

from config import settings


def create_sidebar():
    sb = st.sidebar

    sb.title("An Analysis of Data Science Jobs")

    sb.markdown("----")

    page = sb.radio(label = "Pages", options = settings.RENDERER.get_page_list())

    sb.markdown("""
    ----
    Created by: **Paolo Dano**
    """)

    return page


def main():
    page = create_sidebar()
    settings.RENDERER.render(page)

if __name__ == "__main__":
    main()


