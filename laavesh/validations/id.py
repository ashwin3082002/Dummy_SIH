import re

def check_id_stud(s):
    """
    Checks if ID is valid
    
    ID format : 0000xxxxx0
    0-int
    x-alphabet(a-z, case insensitive)
    """
    if re.search(r'^\d{4}[a-z]{5}\d{1}$', s, re.IGNORECASE):
        return True
    else:
        return False

def parse_id_stud(s):
    """
    Parses the id and returns the year(1234) and serial(abcde) as a dict

    :param s: ID
    :type s: str
    :return: A dict of {'year': 0000 and 'serial' : 'xxxxx'}
    :rtype: dict
    """
    if search := re.search(r'^(\d{4})([a-z]{5}\d{1})$', s, re.IGNORECASE):
        id_temp = list(search.groups())
        return {
            'year':int(id_temp[0]),
            'serial':id_temp[1].lower()    
        }
    else:
        return False

def check_id_insti(s):
    """
    Checks if ID is valid
    
    ID format : xxxxx
    x-alphabet(a-z, case insensitive)
    """
    if re.search(r'^[a-z]{5}$', s, re.IGNORECASE):
        return True
    else:
        return False

def parse_id_insti(s):
    """
    Parses the id and returns the year(1234) and serial(abcde) as a dict

    :param s: ID
    :type s: str
    :return: A dict of {'year': 0000 and 'serial' : 'xxxxx'}
    :rtype: dict
    """
    if search := re.search(r'^([a-z]{5})$', s, re.IGNORECASE):
        id_temp = list(search.groups())
        return {
            'year':int(id_temp[0]),
            'serial':id_temp[1].lower()    
        }
    else:
        return False

inpt = input('Stud ID: ')

print('check_id:', check_id_stud(inpt))
print('parse_id:', parse_id_stud(inpt))

inpt = input('Insti ID: ')