import pytest
from user_registration import (
    validate_first_name,
    validate_last_name,
    validate_email,
    validate_mobile_number,
    valid_password
)

def test_validate_first_name():
    # Valid cases
    assert validate_first_name("John") == True
    assert validate_first_name("Alice") == True
    
    # Invalid cases
    assert validate_first_name("john") == False  
    assert validate_first_name("J") == False     
    assert validate_first_name("Jo") == False    
    assert validate_first_name("1Jo") == False    

def test_validate_last_name():
    # Valid cases
    assert validate_last_name("Smith") == True
    assert validate_last_name("Doe") == True
    
    # Invalid cases
    assert validate_last_name("smith") == False  
    assert validate_last_name("Sm") == False     
    assert validate_last_name("Sm1") == False     
    assert validate_last_name("S") == False      

def test_validate_email():
    # Valid cases
    assert validate_email("abc.xyz@bl.co") == True
    assert validate_email("abc@bl.co") == True
    assert validate_email("abc@bl.co.in") == True
    assert validate_email("abc@bl.coo.in") == True
    
    # Invalid cases
    assert validate_email("abc@bl") == False           
    assert validate_email("abc@.co") == False    
    assert validate_email("abc.xyz@bl.c") == False       

def test_validate_mobile_number():
    # Valid cases
    assert validate_mobile_number("91 9876543210") == True
    assert validate_mobile_number("44 1234567890") == True
    
    # Invalid cases
    assert validate_mobile_number("919876543210") == False 
    assert validate_mobile_number("91 987654321") == False  
    assert validate_mobile_number("91 123456789A") == False    

def test_valid_password():
    # Valid cases
    assert valid_password("Password1!") == True
    assert valid_password("Abcdefg9@") == True
    
    # Invalid cases
    assert valid_password("password1") == False   
    assert valid_password("PASSWORD!") == False
    assert valid_password("Passw1!") == False   
    assert valid_password("Password") == False
