import re
from typing import List, Dict

from error_decorator import input_error


def check_args(args: List[str]) -> None | str:
    """
    Check arguments by patterns.
    :param args: list of arguments
    :return : None if arguments are valid and error message if not.
    """
    name_pattern = r"^[A-Za-z]+$"
    phone_pattern = r"^\+380\d{9}$"
    if not re.match(name_pattern, args[0]) or not re.match(phone_pattern, args[1]):
        return """
        Invalid input.
        Name should contain only alphanumeric characters.
        Phone number should be in format: +380XXXXXXXXX.
        """


@input_error
def add_contact(args: List, contacts: Dict) -> str:
    """
    Add a contact to the dict of contacts
    :param args: list of arguments
    :param contacts: dict of contacts
    """
    valid = check_args(args=args)
    if valid:
        return valid

    name, phone = args
    if name not in contacts.keys():
        contacts[name] = phone
        return "Contact added."
    return "Contact already exists."


@input_error
def change_contact(args: List, contacts: Dict) -> str:
    """
    Change a contact in the dict of contacts
    :param args: list of arguments
    :param contacts: dict of contacts
    """
    valid = check_args(args=args)
    if valid:
        return valid

    name, phone = args
    contact = contacts.get(name)
    if contact:
        contacts[name] = phone
        return "Contact changed."
    return "There is no contact with that name."


@input_error
def print_contact(args: List, contacts: Dict) -> str:
    """
    Print a single contact from the dict of contacts
    :param args: list of arguments
    :param contacts: dict of contacts
    """
    name = args[0]
    return f"{name}: {contacts[name]}"
