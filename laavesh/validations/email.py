import re
from email_validator import validate_email

def check_email(s):
    if re.search(
        r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
        s,
        re.IGNORECASE
    ):
        return True
    else:
        return False

inpt = input('Email: ')
print('check:', check_email(inpt))

# library function : https://stackabuse.com/validate-email-addresses-in-python-with-email-validator/
emailObject = validate_email(inpt)
print(emailObject.email)