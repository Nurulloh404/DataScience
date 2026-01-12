import sys
import os

class Research:
    def __init__(self, path):
        self.file_path = path
        self.data = []

    def file_reader(self, has_header=True):
        with open(self.file_path, 'r') as f:
            self.data = f.read()
            lines = self.data.split('\n')
            if len(lines[0].split(',')) != 2:
                raise Exception("Sarlavha yetarli emas")
            if has_header:
                data_lines = lines[1:]
            else:
                data_lines = lines
            if not data_lines:
                raise Exception("Ma'lumot yetarli emas")
            counter = 0
            data = []
            for line in data_lines:
                if not line: continue
                row = line.split(',')
                if len(row) != 2:
                    raise Exception("Ma'lumot yetarli emas")
                if row[0] not in ['0', '1'] or row[1] not in ['0', '1']:
                    raise Exception("Ma'lumot yetarli emas")
                if row[0] == row[1]:
                    raise Exception("Ma'lumot teng bo'lib qolgan")
                data.append([int(row[0]), int(row[1])])
                counter += 1
            if counter == 0:
                raise Exception("Ma'lumot yetarli emas")
            return data
    class Calculations:
        def counts(self, data):
            heads = 0
            tails = 0
            for line in data:
                if line[0] == 1: heads += 1
                if line[1] == 1: tails += 1
            return heads, tails
        def fractions(self, heads, tails):
            return heads / (heads + tails), tails / (heads + tails)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
        research = Research(path)
        data = research.file_reader()
        calc = research.Calculations()
        heads, tails = calc.counts(data)
        h_frac, t_frac = calc.fractions(heads, tails)
        print(data)
        print(heads, tails) 
        print(round(h_frac, 4), round(t_frac, 4))