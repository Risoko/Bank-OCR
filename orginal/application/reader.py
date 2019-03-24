class ReadLine:

    def __init__(self, nfile):
        self.file = open(nfile)

    def _gen_line(self):
        while True:
            try:
                yield [next(self.file), next(self.file), next(self.file), next(self.file)][:-1]
            except StopIteration:
                self.file.close()
                break
    
    def __iter__(self):
        return self._gen_line()

class ReadNumber:

    def __init__(self, line):
        self.line1, self.line2, self.line3 = line

    def _gen_number(self):
        for idx in range(0, 27, 3):
            yield self.line1[idx:idx+3] + '\n' + self.line2[idx:idx+3] + '\n' + self.line3[idx:idx+3] + '\n'

    def __iter__(self):
        return self._gen_number()
 