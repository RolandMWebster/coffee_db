from abc import ABC, abstractmethod
from datetime import datetime
from pytz import timezone

import streamlit as st

from coffee_db.coffee import Coffee, CoffeeUser, Country, Process, Roastery, Variety
from coffee_db.validate import InputValidator
from coffee_db.database.heroku_psql import CoffeeDB


class EntryForm(ABC):
    """
    An abstract class to represent a streamlit entry form.

    The form should be for a specific CoffeeDB class, and should handle creating streamlit
    forms to add or remove rows from that classes table in the database.

    """

    def __init__(self):
        self.input_validator = InputValidator()
        self.db = CoffeeDB()

    @property
    @abstractmethod
    def header(self):
        """
        Abstract property to define the form header. This should be based on the coffee_db class
         that is represents, eg 'roastery'
        """

        return "default_header"

    @abstractmethod
    def coffee_db_object(self):
        """Abstract method to define the coffee_db class that the form is built for, eg Roastery"""

        pass

    @abstractmethod
    def build_payload(self, **kwargs):
        """Abstract method to build the payload from the use inputs in the streamlit form"""

        pass

    @abstractmethod
    def validate_payload(self, payload: dict):
        """Abstract method to validate the payload using pydantic"""

        pass

    @abstractmethod
    def extract_row_values(self, payload: dict):
        """
        Abstract method to extract values from the payload. These values are what are inserted into
        the database.
        """

        pass

    def add_entry_form(self, **kwargs):
        """Method to build the add entry form, used to add a new row into the database"""

        st.header(self.header.capitalize())

        with st.form(key=f"add_{self.header}", clear_on_submit=True):
            payload = self.build_payload(**kwargs)

            submit = st.form_submit_button("Add")
            if submit:
                validated = self.validate_payload(payload)
                if isinstance(validated, self.coffee_db_object()):
                    message = self.db.insert_row(
                        self.header,
                        self.extract_row_values(payload)
                    )
                    if message:
                        st.warning(message)
                    else:
                        st.experimental_rerun()
                else:
                    st.warning(validated)

    def remove_entry_form(self):
        """Method to buold the remove entry form, used to remove a row from the database"""

        st.header(self.header.capitalize())

        with st.form(key=f"remove_{self.header}", clear_on_submit=True):
            row_id = st.text_input("ID")
            submit = st.form_submit_button("Remove")
            if submit:
                self.db.remove_row(
                    self.header, (int(row_id),)
                )
                st.experimental_rerun()


class RoasteryForm(EntryForm):
    """Class to represent the Roastery form"""

    @property
    def header(self):
        return "roastery"

    def coffee_db_object(self):
        return Roastery

    def build_payload(self, countries: list):
        payload = {"id": 1}  # NOTE: The ID is handled by the database, so is set to a default value here
        payload["name"] = st.text_input("Name")
        payload["country"] = st.selectbox(
            "Country",
            options=countries,
            format_func=lambda x: x.name,
        )

        return payload

    def validate_payload(self, payload: dict):
        return InputValidator.validate_roastery_payload(payload)

    def extract_row_values(self, payload: dict):

        return (
            payload["name"],
            payload["country"].name,
        )


class CountryForm(EntryForm):
    """Class to represent the Country form"""

    @property
    def header(self):
        return "country"

    def coffee_db_object(self):
        return Country

    def build_payload(self):
        payload = {"id": 1}  # NOTE: The ID is handled by the database, so is set to a default value here
        payload["name"] = st.text_input("Name")

        return payload

    def validate_payload(self, payload: dict):
        return InputValidator.validate_country_payload(payload)

    def extract_row_values(self, payload: dict):

        return (
            payload["name"],
        )


class VarietyForm(EntryForm):
    """Class to represent the Variety form"""

    @property
    def header(self):
        return "variety"

    def coffee_db_object(self):
        return Variety

    def build_payload(self):
        payload = {"id": 1}  # NOTE: The ID is handled by the database, so is set to a default value here
        payload["name"] = st.text_input("Name")

        return payload

    def validate_payload(self, payload: dict):
        return InputValidator.validate_variety_payload(payload)

    def extract_row_values(self, payload: dict):

        return (
            payload["name"],
        )


class ProcessForm(EntryForm):
    """Class to represent the Process form"""

    @property
    def header(self):
        return "process"

    def coffee_db_object(self):
        return Process

    def build_payload(self):
        payload = {"id": 1}  # NOTE: The ID is handled by the database, so is set to a default value here
        payload["name"] = st.text_input("Name")

        return payload

    def validate_payload(self, payload: dict):
        return InputValidator.validate_process_payload(payload)

    def extract_row_values(self, payload: dict):

        return (
            payload["name"],
        )


class CoffeeUserForm(EntryForm):
    """Class to represent the CoffeeUser form"""

    @property
    def header(self):
        return "coffee_user"

    def coffee_db_object(self):
        return CoffeeUser

    def build_payload(self):
        payload = {"id": 1}  # NOTE: The ID is handled by the database, so is set to a default value here
        payload["name"] = st.text_input("Name")

        return payload

    def validate_payload(self, payload: dict):
        return InputValidator.validate_coffee_user_payload(payload)

    def extract_row_values(self, payload: dict):

        return (
            payload["name"],
        )


class CoffeeForm(EntryForm):
    """Class to represent the Coffee form"""

    @property
    def header(self):
        return "coffee"

    def coffee_db_object(self):
        return Coffee

    def build_payload(self, coffee_users, countries, roasteries, processes, varieties):
        payload = {"id": 1}  # NOTE: The ID is handled by the database, so is set to a default value here
        payload["name"] = st.text_input("Name")
        payload["country_of_origin"] = st.selectbox(
            "Country of Origin",
            options=countries,
            format_func=lambda x: x.name,
        )
        payload["roastery"] = st.selectbox(
            "Roastery",
            options=roasteries,
            format_func=lambda x: x.name,
        )
        payload["process"] = st.selectbox(
            "Process",
            options=processes,
            format_func=lambda x: x.name,
        )
        payload["varietal"] = st.multiselect(
            "Varietal",
            options=varieties,
            format_func=lambda x: x.name,
        )
        payload["elevation"] = st.text_input("Elevation")
        payload["tasting_notes"] = st.text_input("Tasting Notes")

        for key in ["elevation", "tasting_notes"]:
            if payload[key] == "":
                payload[key] = None

        if payload["varietal"] == []:
            payload["varietal"] = [x for x in varieties if x.name == "Unknown"]

        payload["added_by"] = st.selectbox(
            "Added By",
            options=coffee_users,
            format_func=lambda x: x.name,
        )

        payload["date_added"] = datetime.now(tz=timezone("GMT")).strftime('%Y-%m-%d %H:%M:%S')

        return payload

    def validate_payload(self, payload: dict):
        return InputValidator.validate_coffee_payload(payload)

    def extract_row_values(self, payload: dict):

        return (
            payload["name"],
            payload["country_of_origin"].name,
            payload["roastery"].name,
            payload["process"].name,
            ", ".join([variety.name for variety in payload["varietal"]]),
            payload["elevation"],
            payload["tasting_notes"],
            payload["added_by"].name,
            payload["date_added"],
        )
