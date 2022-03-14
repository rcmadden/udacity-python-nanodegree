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
        # filter category and or year match skip the 2 cases below
        if category and prize['category'].lower() != category.lower():
            continue
        if year and prize['year'] != year:
            continue
       
        # limit results if no filters provided
        if year == None and category == None:
            if count < 10:
                print(f"{prize['year']} {prize['category'].title()}")
                for laureate in prize['laureates']:
                    print(laureate['firstname'], laureate.get('surname'))
                count+=1
                print('')

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