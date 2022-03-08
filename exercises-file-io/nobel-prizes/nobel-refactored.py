import json
from sys import stdout
from textwrap import indent
import helper

#def load_nobel_prizes(filename='../../data/prize.json'):
def load_nobel_prizes(filename='data/prize.json'):
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
        # check if key in dict
        if 'laureates' in prize:
            
            if prize['year'] == year and category == None:
                json.dump(prize, stdout,indent=2)
                count +=1
            
            elif prize['year'] == year and prize['category'] == category:
                json.dump(prize, stdout,indent=2)
                count +=1

            elif year == None and prize['category'] == category:
                json.dump(prize, stdout,indent=2)
                count +=1
            
            elif year == None and category == None:
                while count < 10:
                    json.dump(prize, stdout,indent=2)
                    count+=1
            # print(count, ' Total')
        
        # if key not in dict
        else:
            laureateCount+=1
    
    print('no laureate count: ', laureateCount)
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