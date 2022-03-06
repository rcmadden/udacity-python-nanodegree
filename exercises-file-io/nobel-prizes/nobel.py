import json
import helper


def load_nobel_prizes(filename='../../data/prize.json'):
    with open(filename) as json_file:
        return json.load(json_file)
    


def main(year, category):
    data = load_nobel_prizes()
    prizes = len(data['prizes'])

    if category != None:
        category = category.lower()


    for i in range(prizes):
        if data['prizes'][i]['year'] == year and category == None:
            print(data['prizes'][i])

        elif data['prizes'][i]['year'] == year and data['prizes'][i]['category'] == category:
            print(data['prizes'][i])

        elif year == None and data['prizes'][i]['category'] == category:
            print(data['prizes'][i])
            

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)

