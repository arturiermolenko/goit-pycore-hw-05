from typing import Tuple

from error_decorator import input_error
from handlers import add_contact, change_contact, print_contact


def parse_input(user_input: str) -> Tuple[str, list] | None:
    """
    Take users input as a string and split into separate command and list of args
    :param user_input: string to be parsed
    :return: tuple of command and list of args
    """
    if not user_input:
        return
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def print_hint() -> str:
    return """
        How can I help you?
        
            Type 'add name phone' to add a new contact.
            Type 'change contact phone' to change contact.
            Type 'phone name' to print contacts phone number.
            Type 'all' to print all contacts in phone book
            Type 'close' or 'exit' to exit the assistant. 
            """


@input_error
def main() -> None:
    contacts = {}
    hint = print_hint()
    print(hint)

    while True:
        user_input = input("Enter a command: ")

        parsed_input = parse_input(user_input)
        if parsed_input:
            command, *args = parsed_input
        else:
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "help":
            response = print_hint()
        elif command == "add":
            response = add_contact(args, contacts)
        elif command == "change":
            response = change_contact(args, contacts)
        elif command == "phone":
            response = print_contact(args, contacts)
        elif command == "all":
            response = ""
            for username, phone in contacts.items():
                response += f"{username}: {phone}\n"
            if not response:
                response = "The phone book is empty."
        else:
            response = "Invalid command."

        print(response.strip())


if __name__ == "__main__":
    main()
