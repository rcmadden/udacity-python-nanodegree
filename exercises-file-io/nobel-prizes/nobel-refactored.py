import json
import helper

#def load_nobel_prizes(filename='../../data/prize.json'): # run frorm terminal
def load_nobel_prizes(filename='data/prize.json'): # run with debugger
    with open(filename) as json_file:
        return json.load(json_file)


def main(year, category):
    data = load_nobel_prizes()
    prizes = data['prizes']
    count = 0

    
    for prize in prizes:
        # skip if key not in dict
        if 'laureates' not in prize:
            continue
        # limit results if no filters provided
        if year == None and category == None:
            while count < 10:
                for laureate in prize['laureates']:
                    print(laureate['firstname'], laureate['surname'])
                count+=1
                print('')
        # filter on mathcing year or category and print results
        if (year and prize['year'] == year) or (category and prize['category'].lower() == category.lower()):
            if category and prize['category'].lower() != category.lower():
                continue
            if year and prize['year'] != year:
                continue

            else:
                print(f"{prize['year']} {prize['category'].title()}")
                for laureate in prize['laureates']:
                    print(laureate['firstname'], laureate.get('surname'))     
                count +=1
                print('')

    print(count, ' Total')
            
    
if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)