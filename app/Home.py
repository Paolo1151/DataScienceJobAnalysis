import os

import streamlit as st
from PIL import Image

from config import settings


st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout='centered',
    initial_sidebar_state='auto'
)


with open(os.path.join(settings.CONTENT_PATH, 'home.md'), 'r') as f:
    st.markdown(f.read())

img = Image.open(os.path.join(settings.IMAGE_PATH, 'data_science_home.jpg'))
st.image(img, caption="From https://validitysolutions.us/data-scientist/")

with st.sidebar:
    st.success("Select one of the Pages Above to start!")



