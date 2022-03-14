from ast import Not
import json
from sys import stdout
from textwrap import indent
import helper

#def load_nobel_prizes(filename='../../data/prize.json'): # run frorm terminal
def load_nobel_prizes(filename='data/prize.json'): # run with debugger
    with open(filename) as json_file:
        return json.load(json_file)


def main(year, category):
    data = load_nobel_prizes()
    prizes = data['prizes']
    count = 0
    laureateCount = 0

    # list comprehension
    '''for prize in prizes:
        if prize['year'] == year:
            prize_list.append(prize)
    '''
    # prize_list = [prize for prize in prizes if prize['year'] == year]
    # json.dump(prize_list, stdout,indent=2)
    # print(len(prize_list), ' Total')

    if category != None:
        category = category.lower()
    
    for prize in prizes:
        # skip if key not in dict
        if 'laureates' not in prize:
            continue

        if year == None and category == None:
            while count < 10:
                for laureate in prize['laureates']:
                    print(laureate['firstname'], laureate['surname'])
                count+=1
                print('')
        elif not(year == None and category == None):
            # print the matching year and or category
            if prize['year'] == year and (category == None or prize['category'] == category) or year == None and prize['category'] == category:
                print(f"{prize['year']} {prize['category']}")
                for laureate in prize['laureates']:
                # print(laureate.get('firstname'), laureate.get('surname'))
                    print(laureate['firstname'], laureate.get('surname'))     
                count +=1
                print('')
    
    print(count, ' Total')
            
    

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)