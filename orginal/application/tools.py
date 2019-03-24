from application.settings import ELEMENTS
from application.reader import read_number
from application.check_and_repair_string import check_string

def get_number_account(iterable):
    string = ''
    bad_element = ''
    for output in read_number(iterable):
        helpty_str = str(ELEMENTS.get(output, '?'))
        if helpty_str == '?':
            if len(bad_element) == 0:
                bad_element = output 
            string += '?'
        else:
            string += helpty_str
    return check_string(string, bad_element)


                    

    