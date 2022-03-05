import json
from sys import stdout
from textwrap import indent
import helper

# def load_nobel_prizes(filename='../../data/prize.json'):
def load_nobel_prizes(filename='data/prize.json'):
    with open(filename) as json_file:
        return json.load(json_file)


def main(year, category):
    data = load_nobel_prizes()
    prizes = data['prizes']

    # list comprehension
    prize_list0 = [prize for prize in prizes if prize['year'] == '2021']
    json.dump(prize_list0, stdout,indent=2)
    prize_list1 = []

    # looping list
    for prize in prizes:
        if prize['year'] == '2021':
            prize_list1.append(prize)
    json.dump(prize_list1, stdout, indent=2)
    
    # json_string = json.dumps(data)
    # for prize in prizes:
    #     # print(prize)
    #     if 'laureates' not in prize:
    #         continue
    #     # i = 0
    #     if prize['year'] != year:
    #         continue
    #         # print(prize['year'])
    #         # print(prize['laureates'])
    #     print(f"{prize['year']} Nobel Prize in {prize['category'].title()}")
    #     for laureate in prize['laureates']:
    #         firstname = laureate['firstname']
    #         surname = laureate.get('surname', '')
    #         print(firstname, surname)
    #         # todo print options
    #         print()
    #     print('\n')
            # print(prize['year'], prize['category'])
            # for i in range(len(prize['laureates'])):
            #     if prize.get(['laureates'][i]['surname']) in prize:
            #         print(prize['laureates'][i]['firstname'], prize['laureates'][i]['surname'])
            #     i += i
            # print('\n')
        # for each dict print each laureates firstname surname
        # for laureate in prize['laureates']:
        #     firstname = laureate['firstname']
        #     surname = laureate['surname']

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)