import json
import helper

def load_nobel_prizes(filename='../../../../exercise-data/prize.json'):
    with open(filename) as json_file:
        return json.load(json_file)


def main(year, category):

