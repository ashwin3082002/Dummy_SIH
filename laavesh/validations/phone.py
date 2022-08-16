import re

def check_phn(n):
    """
    Checks if phone number is vaild
    
    ID format : 0000xxxxx0
    0-int
    x-alphabet(a-z, case insensitive)
    """
    if re.search(r'^(?:(?:\+91)|(?:0091))?\d{10}$', n):
    # if re.search(r'^(\+91)\d{10}$', n):
        return True
    else:
        return False

def parse_phn(n):
    """
    Parses the number and returns the number without country code

    :param n: phone number
    :type s: str
    :return: phone number without country code
    :rtype: int
    """
    if search := re.search(r'^(?:(?:\+91)|(?:0091))?(\d{10})$', n):
        phn = list(search.groups())
        return int(phn[0])
    else:
        return False

inpt = input('number: ')
print('check_phn:', check_phn(inpt))
print('parse_phn:', parse_phn(inpt))