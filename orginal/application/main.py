from application.reader import ReadLine
from application.tools import CreateNumberAccount


def scanner_file(file='data.txt', output='result.txt'):
    """Return scanner number account."""
    with open(output, 'w') as f:
        for list_with_line in ReadLine(file):
            f.write(str(CreateNumberAccount(list_with_line).number_account) + '\n') 
    return open(output).read()

if __name__ == '__main__':
    print(scanner_file())


