import os

import streamlit as st

from config import settings


st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout='centered',
    initial_sidebar_state='auto'
)


with open(os.path.join(settings.CONTENT_PATH, 'home.md'), 'r') as f:
    st.markdown(f.read())

with st.sidebar:
    st.success("Select one of the Pages Above to start!")



