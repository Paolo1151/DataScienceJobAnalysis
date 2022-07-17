import os
from enum import Enum

import streamlit as st

from config import settings

class Page(Enum):
    HOME = 0
    BACKGROUND = 1
    ANALYSIS = 2


class Renderer(object):
    def __init__(self):
        self.page_list = []

    def render(self, page_str: str):
        page = Page[page_str.upper()]
        if page == Page.HOME:
            self._render_home()
        elif page == Page.BACKGROUND:
            self._render_background()
        elif page == Page.ANALYSIS:
            self._render_analysis()
        else:
            raise Exception("Unknown page")

    def _render_home(self):
        st.title("Home")

    def _render_background(self):
        st.title("Background")
        with open(os.path.join(settings.CONTENT_PATH, "background.md"), "r") as f:
            st.markdown(f.read())

    def _render_analysis(self):
        st.title("Analysis")

    @staticmethod
    def get_page_list():
        return list(map(lambda x: x.name.capitalize(), Page))