import sys
from random import randint

class Research:
    def __init__(self, path):
        self.file_path = path

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
        def __init__(self, data):
            self.data = data
        
        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            return heads / total, tails / total

    class Analytics(Calculations): 
        def predict_random(self, num):
            predictions = []
            for i in range(num):
                rand = randint(0, 1)
                if rand == 1:
                    predictions.append([1, 0])
                else:
                    predictions.append([0, 1])
            return predictions

        def predict_last(self):
            return self.data[-1]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
        
        res = Research(path)
        data = res.file_reader()
        
        an = res.Analytics(data)
        
        heads, tails = an.counts()
        
        h_frac, t_frac = an.fractions(heads, tails)
        
        print(data)
        print(heads, tails)
        print(h_frac, t_frac)
        print(an.predict_random(3))
        print(an.predict_last())