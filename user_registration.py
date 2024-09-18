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

    if not pattern.match(first_name) :
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

    if not pattern.match(last_name) :
        print(f"Last name: {last_name} is invalid.",
              "\nName must start with Capital and atleast have 3 characters.")

def validate_email(email):
    """
    Description:
        Validates the email address based on the following rules:
        - Email must have three mandatory parts (abc, bl, co).
        - Email can have two optional parts (xyz, in).
        - The '@' symbol must separate the local part and the domain.
        - Dots must be positioned correctly between sections.
    Parameters:
        email (str): The email address to be validated.
    Return:
        bool: Returns True if the email is valid, otherwise False.
    """
    pattern = re.compile(r'^([a-zA-Z0-9]{3,})+(\.[a-zA-Z0-9]+)?@[a-zA-Z]{2,}\.[a-z]{2,}(?:\.[a-zA-Z]{2,})?$')
    if not pattern.match(email):
        print(f"Email: {email} is invalid.")

def validate_mobile_number(mobile_number):
    """
        Description:
            Validates the mobile number based on
            - The string must start with two digits (e.g., a country code).
            - Followed by a single space.
            - Then, exactly ten digits (which could represent a phone number).
        Parameters:
        mobile number (str): The mobile number to be validated.
        Return:
            bool: Returns True if the email is valid, otherwise False.
    """
    pattern = re.compile(r'^[0-9]{2}\s[0-9]{10}$')

    if not pattern.match(mobile_number):
        print(f"Mobile Number: {mobile_number} is invalid.")


def user_registration_form():
    """
    Description:
        Takes user input for fields in rgistration form.
    Parameters:
        None
    Return:
        returns if input is valid or not.
    """
    first_name = input("Enter your first name: ")
    validate_first_name(first_name)

    last_name = input("Enter your last name: ")
    validate_last_name(last_name)

    email = input("Enter your email: ")
    validate_email(email)

    mobile_number = input("Enter your mobile number: ")
    validate_mobile_number(mobile_number)


user_registration_form()