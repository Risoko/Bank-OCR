from application.settings import POSIBLE_OPTIONS, ELEMENTS

class Debugger:

    def __init__(self, string, bad_elements):
        try:
            self.bad_elements = bad_elements[0]
        except IndexError:
            pass
        self.string = self._check_error(string)
        
    def _check_error(self, string):
        if string.count('?') > 1:
            return string + ' ' + 'ILL'
        if '?' in string:
            string = self._repair_ILL(string)
        if self._get_sum_control([int(element) for element in string]) % 11 != 0:
            string = self._repair_ERR(string)
        return string

    def _repair_ILL(self, string):
        helpty = []
        for key, value in ELEMENTS.items():
            if self._get_number_maching_elements(key) == 1:
                copy = string
                idx = copy.index('?')
                copy = copy[:idx] + str(value) + copy[idx+1:]
                if self._get_sum_control([int(element) for element in copy]) % 11 == 0:
                    return copy
                else:
                    helpty.append(value)
        idx = string.index('?')
        return string[:idx] + str(max(helpty, key=lambda element: len(POSIBLE_OPTIONS.get(element, [])))) + string[idx+1:]

    def _get_number_maching_elements(self, key):
        maching_elements = 0
        for bad_element, correct_element in zip(self.bad_elements, key):
            if bad_element == correct_element:
                maching_elements += 1
        return len(key) - maching_elements

    def _repair_ERR(self, string):
        main_list = []
        for idx, element in enumerate(string):
            help_list = POSIBLE_OPTIONS.get(int(element), [])
            for posible_element in help_list:
                copy = string
                copy  = copy[:idx] + str(posible_element) + copy[idx+1:]
                if self._get_sum_control([int(element) for element in copy]) % 11 == 0:
                    main_list.append(copy)
        if main_list:
            return string +  " " + "AMB" + ' ' + str(sorted(main_list))
        else:
            return string + " " + 'ERR'

    def _get_sum_control(self, lista):
        return sum([idx * int(element) for idx, element in enumerate(reversed(lista), 1)]) 
