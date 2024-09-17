import re

def validate_first_name(first_name):
    """
    Description:
        Validates the first name based on specific rules:
        - The first name must start with a capital letter.
        - The first name must have a minimum of 3 characters.
    Parameters:
        first_name (str): The first name to be validated.
    Return:
        bool: Returns True if the first name is valid, otherwise False.
    """
    pattern = re.compile(r'^[A-Z][a-z]{2,}$')

    if pattern.match(first_name) :
        print(f"First name: {first_name} is valid.")
    else :
        print(f"First name: {first_name} is invalid.",
              "\nName must start with Capital and atleast have 3 characters.")

def validate_last_name(last_name):
    """
    Description:
        Validates the last name based on specific rules:
        - The last name must start with a capital letter.
        - The last name must have a minimum of 3 characters.
    Parameters:
        last_name (str): The last name to be validated.
    Return:
        bool: Returns True if the last name is valid, otherwise False.
    """
    pattern = re.compile(r'^[A-Z][a-z]{2,}$')

    if pattern.match(last_name) :
        print(f"Last name: {last_name} is valid.")
    else :
        print(f"Last name: {last_name} is invalid.",
              "\nName must start with Capital and atleast have 3 characters.")


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
validate_first_name(first_name)
validate_last_name(last_name)
