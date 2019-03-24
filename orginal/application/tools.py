from application.settings import ELEMENTS
from application.reader import ReadNumber
from application.check_and_repair_string import Debugger

class CreateNumberAccount:

    def __init__(self, line):
        self.gen = ReadNumber(line)
        self.bad_element = []
        self.number_account = self._get_number()
    
    
    def _get_number(self):
        string = ''
        for output in self.gen:
            helpty_str = str(ELEMENTS.get(output, '?'))
            if helpty_str == '?':
                self.bad_element.append(output)
                string += '?'
            else:
                string += helpty_str
        return Debugger(string, self.bad_element).string


                    

    