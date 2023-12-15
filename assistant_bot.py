"""This module provides a simple console-based assistant bot."""


def input_error(func):
    """
    Decorator to handle exceptions and provide user-friendly error messages.

    Args:
    func (function): The function to be decorated.

    Returns:
    function: The inner wrapped function.
    """

    def error_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid user name."
        except ValueError:
            return "Please provide both name and phone number."
        except IndexError:
            return "Invalid input format."

    return error_func


@input_error
def add_contact(data, phonebook):
    """Add a new contact to the phonebook.

    Args:
    args (str): The name and phone number of the contact.
    phonebook (dict): The phonebook to add the contact to.

    Returns:
    str: Confirmation message.
    """

    name, number = data.split(" ", 1)
    if name in phonebook:
        return f"Contact {name} already exists."
    phonebook[name] = number
    return f"Contact {name} added."


@input_error
def change_contact(data, phonebook):
    """Change the phone number of an existing contact.

    Args:
    args (str): The name and new phone number of the contact.
    phonebook (dict): The phonebook where the contact is stored.

    Returns:
    str: Confirmation message.
    """

    name, number = data.split(" ", 1)
    if name in phonebook:
        phonebook[name] = number
        return f"Contact {name} updated."
    return "Contact not found."


@input_error
def show_phone(name, phonebook):
    """Retrieve and display the phone number for a given contact name.

    Args:
    name (str): The name of the contact.
    phonebook (dict): The phonebook where the contact is stored.

    Returns:
    str: The phone number of the contact.
    """

    return phonebook[name]


@input_error
def show_all(phonebook):
    """Display all contacts and their phone numbers stored in the phonebook.

    Args:
    phonebook (dict): The phonebook containing contacts and their numbers.

    Returns:
    str: A string containing all contacts and their numbers.
    """

    return "\n".join(
        [f"{name}: {number}" for name, number in phonebook.items()])


def main():
    """
    The main function to run the assistant bot.
    """

    phonebook = {}
    commands = {
        "hello": lambda _: "Hello! How can I help you?",
        "add": lambda data: add_contact(data, phonebook),
        "change": lambda data: change_contact(data, phonebook),
        "phone": lambda data: show_phone(data, phonebook),
        "show all": lambda _: show_all(phonebook),
        "good bye": lambda _: "Good bye!",
        "close": lambda _: "Good bye!",
        "exit": lambda _: "Good bye!"
    }

    while True:
        input_data = input("Enter command: ")
        if input_data.lower() in ["good bye", "close", "exit"]:
            print(commands[input_data.lower()](None))
            break
        if input_data.lower() in ["hello", "show all"]:
            print(commands[input_data.lower()](None))
        else:
            command, *data = input_data.split(maxsplit=1)
            data = " ".join(data)
            if command.lower() in commands:
                print(commands[command.lower()](data))
            else:
                print("Unknown command. Try again.")


if __name__ == "__main__":
    main()
