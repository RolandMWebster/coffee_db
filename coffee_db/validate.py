import datetime
import json
from typing import List

from pydantic import ValidationError
from pydantic.main import ModelMetaclass

from coffee_db.coffee import (
    Coffee,
    CoffeeUser,
    Country,
    Process,
    Roastery,
    Variety,
)


def validate_payload(payload: dict, pydantic_class: ModelMetaclass):
    """Validate a given payload with a pydantic class"""

    try:
        return pydantic_class(**payload)
    except ValidationError as e:
        errors = json.loads(e.json())
        message = str([error["msg"] for error in errors]).lstrip("[").rstrip("]")
        return message


class InputValidator:

    @staticmethod
    def validate_country_payload(payload: dict):
        return validate_payload(payload, Country)

    @staticmethod
    def validate_roastery_payload(payload: dict):
        return validate_payload(payload, Roastery)

    @staticmethod
    def validate_variety_payload(payload: dict):
        return validate_payload(payload, Variety)

    @staticmethod
    def validate_process_payload(payload: dict):
        return validate_payload(payload, Process)

    @staticmethod
    def validate_coffee_user_payload(payload: dict):
        return validate_payload(payload, CoffeeUser)

    @staticmethod
    def validate_coffee_payload(payload: dict):
        return validate_payload(payload, Coffee)
 