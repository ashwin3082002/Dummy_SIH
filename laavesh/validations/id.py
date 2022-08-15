import re

def check_id(s):
    """
    Checks if ID is valid
    
    ID format : 0000xxxxx
    0-int
    x-alphabet(a-z, case insensitive)
    """
    if re.search(r'^\d{4}[a-z]{5}$', s, re.IGNORECASE):
        return True
    else:
        return False

def parse_id(s):
    """
    Parses the id and returns the year(1234) and serial(abcde) as a dict

    :param s: ID
    :type s: str
    :return: A dict of {'year': 0000 and 'serial' : 'xxxxx'}
    :rtype: dict
    """
    if search := re.search(r'^(\d{4})([a-z]{5})$', s, re.IGNORECASE):
        id_temp = list(search.groups())
        return {
            'year':int(id_temp[0]),
            'serial':id_temp[1]    
        }
    else:
        return False

inpt = input('ID: ')

print('check_id:', check_id(inpt))
print('parse_id:', parse_id(inpt))