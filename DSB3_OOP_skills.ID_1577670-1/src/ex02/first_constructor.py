import sys
import os

class Research:
    def __init__(self, path):
        self.file_path = path
        self.data = []

    def file_reader(self):
        with open(self.file_path, 'r') as f:
            self.data = f.read()
            lines = self.data.split('\n')
            if len(lines[0].split(',')) != 2:
                raise Exception("Sarlavha yetarli emas")
            data_lines = lines[1:]
            if not data_lines:
                raise Exception("Ma'lumot yetarli emas")
            counter = 0
            for line in data_lines:
                if not line: continue
                row = line.split(',')
                if len(row) != 2:
                    raise Exception("Ma'lumot yetarli emas")
                if row[0] not in ['0', '1'] or row[1] not in ['0', '1']:
                    raise Exception("Ma'lumot yetarli emas")
                if row[0] == row[1]:
                    raise Exception("Ma'lumot teng bo'lib qolgan")
                counter += 1
            if counter == 0:
                raise Exception("Ma'lumot yetarli emas")
        return self.data

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print(Research(path).file_reader())
