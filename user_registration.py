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
        return True
    else:
        return False

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
        return True
    else:
        return False

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
    if pattern.match(email):
        return True
    else:
        return False
    
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
            bool: Returns True if the mobile is valid, otherwise False.
    """
    pattern = re.compile(r'^[0-9]{2}\s[0-9]{10}$')

    if pattern.match(mobile_number):
        return True
    else:
        return False

def valid_password(password):
    """
    Description:
        Validates the password based on the following rule:
        - The password must contain at least 8 characters.
        - at least one uppercase(lookahead assertion is used)
        - at least one numeric character
    Parameters:
        password (str): The password to be validated.
    Return:
        bool: Returns True if the password is valid, otherwise False.
    """
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8,}$')

    if pattern.match(password):
        return True
    else:
        False


def user_registration_form():
    """
    Description:
        Takes user input for fields in rgistration form.
    Parameters:
        None
    Return:
        returns if input is valid or not.
    """
    # while True:
    #     first_name = input("Enter your first name: ")
    #     if validate_first_name(first_name):
    #         print(f"First name {first_name} is valid.")
    #         break
    #     else:
    #         print(f"First name {first_name} is invalid.")
    
    # while True:
    #     last_name = input("Enter your last name: ")
    #     if validate_last_name(last_name):
    #         print(f"Last name {last_name} is valid.")
    #         break
    #     else:
    #         print(f"Last name {last_name} is invalid.")
    # while True:
    #     email = input("Enter your email: ")
    #     if validate_email(email):
    #         print(f"Email {email} is valid.")
    #         break
    #     else:
    #         print(f"Email {email} is invalid.")
    
    # while True:
    #     mobile_number = input("Enter your mobile number: ")
    #     if validate_mobile_number(mobile_number):
    #         print(f"Mobile number {mobile_number} is valid.")
    #         break
    #     else:
    #         print(f"Mobile number {mobile_number} is invalid.")

    while True:
        password = input("Enter your password: ")
        if valid_password(password):
            print(f"Password {password} is valid.")
            break
        else:
            print(f"Password {password} is invalid.")


user_registration_form()