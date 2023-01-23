import streamlit as st
from typing import Optional

from coffee_db.app.utils import Page


class Site:

    def __init__(self, pages: list[Page], name: str, content_name: str):
        self.pages = pages
        self.name = name
        self.content_name = content_name

    def _get_page_by_name(self, page_name) -> Optional[Page]:
        for page in self.pages:
            if page.NAME == page_name:
                return page
        return None

    def write(self):
        current_page_name = st.sidebar.radio(
            label=" ",
            options=[page.NAME for page in self.pages],
            label_visibility="hidden"
        )
        current_page = self._get_page_by_name(current_page_name)
        current_page.write()
