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
        if prize['year'] == year and category == None:
            print(f"{prize['year']} {prize['category']}")
            for laureate in prize['laureates']:
              # print(laureate.get('firstname'), laureate.get('surname'))
                print(laureate['firstname'], laureate['surname'])     
            count +=1
            print('')
        
        elif prize['year'] == year and prize['category'] == category:
            for laureate in prize['laureates']:
                print(laureate['firstname'], laureate['surname'])
            count +=1
            print('')

        elif year == None and prize['category'] == category:
            for laureate in prize['laureates']:
                print(laureate['firstname'], laureate['surname'])
            count +=1
            print('')

        elif year == None and category == None:
            while count < 10:
                for laureate in prize['laureates']:
                    print(laureate['firstname'], laureate['surname'])
                count+=1
                print('')
    
    print(count, ' Total')
            
    
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