from random import randint
import logging
import urllib.request
import urllib.parse
import json
import config

class Research:
    def __init__(self, path):
        logging.info("Initializing Research class with path: %s", path)
        self.file_path = path

    def file_reader(self, has_header=True):
        logging.info("Reading file: %s", self.file_path)
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
            logging.info("File read successfully, found %d lines", len(data))
            return data

    def send_telegram_message(self, message):
        logging.info("Sending Telegram message: %s", message)
        url = f"https://api.telegram.org/bot{config.telegram_token}/sendMessage"
        data = {
            "chat_id": config.telegram_chat_id,
            "text": message
        }
        try:
            headers = {'Content-Type': 'application/json'}
            req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), headers)
            # We don't verify SSL for simplicity in some envs, but default is secure.
            with urllib.request.urlopen(req) as response:
                if response.status != 200:
                    logging.error("Failed to send Telegram message: Status %s", response.status)
                else:
                    logging.info("Telegram message sent successfully")
        except Exception as e:
            logging.error("Error sending Telegram message: %s", e)

class Calculations:
    def __init__(self, data):
        logging.info("Initializing Calculations class")
        self.data = data
    
    def counts(self):
        logging.info("Calculating counts of heads and tails")
        heads = sum(row[0] for row in self.data)
        tails = sum(row[1] for row in self.data)
        return heads, tails

    def fractions(self, heads, tails):
        logging.info("Calculating fractions")
        total = heads + tails
        return heads / total, tails / total

class Analytics(Calculations): 
    def predict_random(self, num):
        logging.info("Predicting random outcomes for %d steps", num)
        predictions = []
        for i in range(num):
            rand = randint(0, 1)
            if rand == 1:
                predictions.append([1, 0])
            else:
                predictions.append([0, 1])
        return predictions

    def predict_last(self):
        logging.info("Getting last prediction")
        return self.data[-1]

    def save_file(self, data, filename, extension):
        logging.info("Saving report to file: %s.%s", filename, extension)
        with open(f"{filename}.{extension}", "w") as f:
            f.write(data)