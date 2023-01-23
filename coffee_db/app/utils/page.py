from abc import ABC, abstractmethod
import streamlit as st

from coffee_db.app.utils import Tab


class Page(ABC):

    NAME: str

    @abstractmethod
    def __init__(self, tabs: list[Tab] = None):
        self.tabs = tabs

    @abstractmethod
    def write(self):
        pass

    def write_tabs(self):
        if self.tabs is not None:
            tabs = st.tabs([tab.NAME for tab in self.tabs])
            for i, tab in enumerate(tabs):
                with tab:
                    self.tabs[i].write()

    def __str__(self):
        return self.NAME
