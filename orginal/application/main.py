from application.reader import read_line
from application.tools import get_number_account


def scanner_file(file='data.txt', output='result.txt'):
    """Return scanner number account."""
    f1 = open(file)
    with open(output, 'w') as f:
        for list_with_line in read_line(f1):
            f.write(str(get_number_account(list_with_line) + '\n')) 
        f1.close()
    return open(output).read()
if __name__ == '__main__':
    print(scanner_file())


