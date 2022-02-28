import json
import os
import argparse
import helper


def load_approaches():
    with open('data/cad.json') as f:
        return json.load(f)

def main(year, category):
    data = load_approaches()
    print(data['fields'])
    print((data['data'][0]))
    return

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)