import csv
import json

import helper

# def read_airlines(filename='airlines.dat'): # from terminal
def read_airlines(filename='exercises-file-io/airport-routes/airlines.dat'): # from vs code

    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1] # key to value map
    return airlines # dict of key value pairs


# def read_airports(filename='airports_partial.dat'):
def read_airports(filename='exercises-file-io/airport-routes/airports_partial.dat'):
    # Return a map of code -> name
    airports = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1] # airport name to icao code
    return airports


def read_routes(filename='routes_partial.dat'):
    # Return a map from source -> list of destinations
    return {}


def find_paths(routes, source, dest, max_segments):
    # Run a graph search algorithm to find paths from source to dest.
    return {}

def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    print(len(airlines))
    airports = read_airports()
    print(len(airports))
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Build a collection of output paths!
    
    # Don't forget to write the output to JSON!

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
