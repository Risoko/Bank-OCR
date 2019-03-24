def read_line(nfile):
    list_with_line = []
    for line in nfile:
        list_with_line.append(line)
        if len(list_with_line) == 4:
            yield list_with_line[:-1]
            list_with_line = []

def read_number(iterable):
    line1, line2, line3 = iterable
    for idx in range(0, 27, 3):
        yield line1[idx:idx+3] + '\n' + line2[idx:idx+3] + '\n' + line3[idx:idx+3] + '\n'

 