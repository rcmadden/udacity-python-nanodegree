import csv
import json
from signal import pause

import helper

# def read_airlines(filename='airlines.dat'): # from terminal
def read_airlines(filename='exercises-file-io/airport-routes/airlines.dat'): # from vs code

    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1] # key to value map
    return airlines # dict of key value pairs
    # airlines = {'N/A': 'Private flight', 'GNL': '135 Airways', 'RNX': '1Time Airline'}

# def read_airports(filename='airports_partial.dat'):
def read_airports(filename='data/airports.dat'):
    # Return a map of code -> name
    airports = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1] # airport name to icao code
    return airports
    # airports = {'LFR': 'La Fria Airport', '\\N': 'Oswego County Airport', 'MAR': 'La Chinita Internati...al Airport'}
    
def read_routes(filename='data/routes.dat'):
    # Return a map from source -> list of destinations
    routes = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            if routes.get(line[2]):
                routes[line[2]] += [line[4]]
            else:
                routes[line[2]] = [line[4]]
    return routes
# len(routes['SFO']) 111
# len(routes['SGN'])  57
# {'SFO': ['GDL', 'HKG', 'HNL', 'IAD', 'IAH', 'ICN', 'IND', 'JFK', 'KIX', ...], 
# 'SGF': ['DEN', 'ORD', 'DFW', 'ORD'], 
# 'SGN': ['HKG', 'DME', 'BKK', 'BMV', 'CXR', 'DAD', 'DLI', 'HAN', 'HPH', ...], 
# 'SGU': ['DEN'], 
# 'SHD': ['IAD'],
# 'BOS': ['LHR', 'BUF', 'CLT', 'CUN', 'DCA', 'DFW', 'JFK', 'LAX', 'LGA', 'MDT', 'MIA', 'ORD', 'PHL', 'PHX', ...]}


def find_paths(routes, source, dest, max_segments):
    # Run a graph search algorithm to find paths from source to dest.
    # Start at the source airport. The only zero-length path is the empty path.
    path = routes[source]
    segements = {}
    # Start at the source airport. The only zero-length path is the empty path.
    ## 'SFO': ['GDL', 'HKG', 'HNL', 'IAD', 'IAH', 'ICN', 'IND', 'JFK', 'KIX', ...]

    # For each path of length n, from 0 to 1 less than the total number of segments
    ## 'GDL': []
    # Find all neighbors of any airports reachable at the end of a path of length n
    # These are the paths of length n + 1
    # Return any and all paths of length <= n that end in the target airport.
    return {}

def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    print(len(airlines))
    airports = read_airports()
    print(len(airports))
    # print(airports['BOS'])
    # print(airports['SFO'])
    routes = read_routes()
    # print('routes BOS: ',routes['BOS'])
    # print(routes['SFO'])

    # print('BOS')
    # for code in routes['BOS']:
    #     print('BOS', code, airports.get(code))

    # print('SFO')
    # for code in routes['SFO']:
    #     print('SFO', code, airports.get(code))
    
    print('LHR')
    for code in routes['LHR']:
        print('LHR', code, airports.get(code))
    
    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Build a collection of output paths!
    
    # Don't forget to write the output to JSON!

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
